def strip_fence(text):
    text = text.strip(' \n')
    if text.startswith('```'):
        i = text.find('\n')
        text = text[i+1:]
    
    if text.endswith('```'):
        i = text.rfind('\n')
        text = text[:i]
    
    return text
