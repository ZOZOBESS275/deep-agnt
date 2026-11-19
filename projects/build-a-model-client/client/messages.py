def user_message(text):
    return {'role':'user', 'content':text}


def assistant_message(text):
    return {'role':'assistant', 'content': text}


def add_turn(history, question, answer):
    new_history = history + [user_message(question)] + [assistant_message(answer)]  
    return new_history
