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
    
    conversation = list(messages)
    parts = []

    for _ in range(max_continues + 1):
        reply = call(conversation)
        chunk = text_of(reply)
        parts.append(chunk)

        if not is_cut_off(reply):
            return "".join(parts), True

        conversation.extend([
            assistant_message(chunk),
            user_message(CONTINUE),
        ])

    return "".join(parts), False
