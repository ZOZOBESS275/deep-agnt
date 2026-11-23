def strip_fence(text):
    text = text.strip(' \n')
    if text.startswith('```'):
        i = text.find('{')
        text = text[i:]
    
    if text.endswith('```'):
        i = text.find('}')
        text = text[:i+1]
    
    return text
