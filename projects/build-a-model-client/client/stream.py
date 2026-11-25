def text_delta(event):
    
    delta = event.get('delta',[])
    
    if delta ==[]:
        return ''
    
    if delta.get('type','')=='text_delta':
        return delta['text'] 
    
    else:
        return ''


def join_stream(events):
    
    list_delta = [text_delta(event) for event in events]
        
    return ''.join(list_delta)
