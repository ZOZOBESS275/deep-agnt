def text_of(reply):
    list_of_reply = [text['text'] for text in reply.get('content',[]) if text['type']=='text']
    return "".join(list_of_reply)


def is_cut_off(reply):
    if reply.get('stop_reason',[])=='max_tokens':
        return True
    else:
        return False


def usage_of(reply):
    input_token = 0
    output_token = 0

    if 'input_tokens' in reply.get('usage',[]):
        input_token = reply['usage']['input_tokens']
    if 'output_tokens' in reply.get('usage',[]):
        output_token = reply['usage']['output_tokens']
    
    return (input_token, output_token)


def ask(model, messages, system=None, max_tokens=300):
    return model.chat(messages=messages, system=system, max_tokens=max_tokens)


CONTINUE = "Continue exactly where you stopped. Repeat nothing."


def ask_whole(call, messages, max_continues=2):
    
    reply = None
    temp = ""
    
    while max_continues!=0:

        reply = call(messages)
        
        if len(messages)>1:
            max_continues-=1
            if max_continues==0:
                break
        # print(reply)
        if is_cut_off(reply)==True:
            messages = messages + [assistant_message(text_of(reply))] + [user_message(CONTINUE)] 
            temp += text_of(reply)
            
        else:
            return ("".join([temp,text_of(reply)]), True)
    
    return ("".join([temp,text_of(reply)]), False)
