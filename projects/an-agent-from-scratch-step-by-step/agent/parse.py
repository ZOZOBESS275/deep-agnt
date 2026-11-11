def text_blocks(response):
    
    result = []
    
    for text_block in response.get('content',[]):
        if 'text' in text_block:
            result.append(text_block['text'])
    
    return result


def text_of(response):
    return '\n'.join(text_blocks(response)).strip()


def tool_uses(response):
    return [block for block in response.get('content',[]) if 'tool_use' in block['type']]


def wants_tool(response):
    if 'tool_use' in response.get('stop_reason',[]):
        return True
    else:
        return False


def assistant_message(response):
     return {'role':'assistant', 'content': response.get('content',[])}
