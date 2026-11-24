def strip_fence(text):
    text = text.strip(' \n')
    if text.startswith('```'):
        i = text.find('{')
        text = text[i:]
    
    if text.endswith('```'):
        i = text.find('}')
        text = text[:i+1]
    
    return text


import json


def parse_json(text):
    # return text
    text = strip_fence(text)
    start = text.find('{')
    end = text.find('}')

    if start==-1 or end ==-1 or start>end:
        return None
    else:
        try:
            return json.loads(text[start:end+1])
        
        except ValueError as e:
            return None
