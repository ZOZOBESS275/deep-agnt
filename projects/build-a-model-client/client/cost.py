def price_call(input_tokens, output_tokens, price):
    
    input_cost = input_tokens * price.get('input',0)
    output_cost = output_tokens * price.get('output',0)
    cost = (input_cost+output_cost)/1000000
    if cost > 0 and cost < 1:
        return 1
    elif cost > 1:
        return round(cost)
    else:
        return 0
