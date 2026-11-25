def text_delta(event):
    
    delta = event.get('delta',{})
    
    if delta.get('type')=='text_delta':
        return delta.get('text','') 
    
    return ''


def join_stream(events):
    
    list_delta = [text_delta(event) for event in events]
        
    return ''.join(list_delta)


def stop_reason_of(events):
    
    reason_stop = next(
    (
        event.get("delta", {}).get("stop_reason")
        for event in events
        if event.get("type") == "message_delta"
        ),
        None,
    )
    
    return reason_stop
