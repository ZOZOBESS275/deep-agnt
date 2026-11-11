def user_message(text):
    return {'role':'user', 'content':text}


def results_message(results):
    return user_message(results)


def handle_tool_turn(reply, messages, tools):
    
    result = []
    messages.append(assistant_message(reply)) 
    tools_used = tool_uses(reply)

    
    for tool_u in tools_used:
        messages.append(results_message([run_tool(tool_u,tools)]))
        result.append(run_tool(tool_u,tools))

    return result


def run_agent(task, model, tools, specs, max_turns=6):
    
    
    messages = [user_message(task)]
    for i in range(max_turns):

        reply = model.chat(messages, tools=specs)
        
        if wants_tool(reply):
            result = handle_tool_turn(reply, messages,tools) 
                    
        else:
            return text_of(reply)
    
    return None
