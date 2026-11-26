def price_call(input_tokens, output_tokens, price):
    
    input_cost = input_tokens * price.get('input',0)
    output_cost = output_tokens * price.get('output',0)
    cost = (input_cost+output_cost)/1000000
    
    if cost <= 0:
        return 0
    return max(1, round(cost))
