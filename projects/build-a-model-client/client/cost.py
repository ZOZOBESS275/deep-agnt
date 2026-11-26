def price_call(input_tokens, output_tokens, price):
    
    input_cost = input_tokens * price.get('input',0)
    output_cost = output_tokens * price.get('output',0)
    cost = (input_cost+output_cost)/1000000
    
    if cost <= 0:
        return 0
    return max(1, round(cost))


EMPTY_LEDGER = {"calls": 0, "input_tokens": 0, "output_tokens": 0, "micro": 0}


def add_call(ledger, reply, price):
    
    new_ledger = ledger.copy()
    new_ledger['calls'] +=1
    input_tokens, output_tokens = usage_of(reply) 
    new_ledger['input_tokens'] += input_tokens
    
    new_ledger['output_tokens'] += output_tokens
    
    new_ledger['micro']=price_call(new_ledger['input_tokens'], new_ledger['output_tokens'],price)

    return new_ledger
