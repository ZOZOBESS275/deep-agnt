def tool_spec(name, description, properties=None, required=None):
    if properties==None:
        properties={}
    if required==None:
        required=[]
    
    return {
        'name':name, 
        'description':description,
        'input_schema':{
            'type':'object',
            'properties':properties,
            'required':required
        }
    }


def tool_specs():
    return [
        tool_spec('list_files', None, None, None),
        tool_spec('read_file', None, None, ['path']),
        tool_spec('write_file', 'tests/., complete', ['content','path'], ['path', 'content']),
        tool_spec('grep', None, None, ['pattern']),
        tool_spec('run_tests', None, None, None)
    ]
