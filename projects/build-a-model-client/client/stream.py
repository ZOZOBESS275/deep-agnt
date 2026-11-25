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


def stop_reason_of(events):
    
    reason_stop = [event.get('delta',None)['stop_reason'] for event in events if event['type']=='message_delta']

    if reason_stop==[]:
        return None
    return "".join(reason_stop)
