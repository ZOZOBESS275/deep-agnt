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
