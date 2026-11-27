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
    
    ask_func = lambda: ask(client['model'], messages=messages,system=client['system'])

    reply = call_with_retry(fn=ask_func, sleep = client['sleep'])



    client['ledger'] = add_call(client['ledger'], reply, client['price'])

    return reply
