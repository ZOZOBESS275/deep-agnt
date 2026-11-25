def text_delta(event):
    
    delta = event.get('delta',[])
    
    if delta ==[]:
        return ''
    
    elif delta['type']=='text_delta':
        return delta['text'] 
    
    else:
        return ''
