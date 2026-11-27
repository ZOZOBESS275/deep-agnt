import time


def new_client(model, price, system=None, sleep=time.sleep):
    return {
        'model': model,
        'price': price,
        'system': system,
        'sleep': sleep,
        'history': [],
        'ledger': EMPTY_LEDGER.copy()
    }


def call(client, messages):
    
    reply = call_with_retry(fn=lambda: ask(client['model'], messages=messages,system=client['system']),
     sleep = client['sleep']
     )
    
    client['ledger'] = add_call(client['ledger'], reply, client['price'])

    return reply


def send(client, text):
    
    messages = client['history'] + [user_message(text)]

    reply, _ = ask_whole(lambda msgs:call(client,msgs),messages)

    client['history'] = add_turn(client['history'], text, reply)

    return reply


def send_json(client, prompt, schema):
    
    reply = ask_json(lambda msgs: call(client,msgs), prompt, schema)

    return reply
