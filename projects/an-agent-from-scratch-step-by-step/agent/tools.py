def param_schema(kind, description):
    return {'type':kind, 'description':description}


def required_params(params):
    result = []

    return [param for param in params.keys() if params.get(param)[2]==True]


def tool_spec(name, description, params):
    
    proporty = {}

    for i ,(k,v) in enumerate(params.items()):
        proporty.update({k:param_schema(v[0],v[1])})
    result = {'name':name,
        'description':description,
        'input_schema':{'type':'object',
        'properties':proporty,
        'required':required_params(params)}}
    return result


def tool_result(tool_use_id, content, is_error=False):
    
    result = {'type':'tool_result', 'tool_use_id': tool_use_id,'content':str(content)}

    if is_error:
        result.update({'is_error':is_error})  

    return result


def run_tool(block, registry):
    
    
    try:    
        callable_func = registry[block['name']]
    
        return tool_result(block['id'],callable_func(**block['input']))
    except KeyError as e:
        return tool_result(block['id'],f"unknown tool '{block['name']}'", is_error=True)
    
    except ZeroDivisionError as e:
        return tool_result(block['id'], f'{type(e).__name__}: {str(e)}', is_error=True)
