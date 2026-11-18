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
