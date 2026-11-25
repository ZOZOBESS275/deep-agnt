def text_delta(event):
    
    delta = event.get('delta',None)
    
    if delta ==None:
        return ''
    
    elif delta['type']=='text_delta':
        return delta['text'] 
    
    else:
        return ''
