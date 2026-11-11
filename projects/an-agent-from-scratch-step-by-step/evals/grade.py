def parse_trace_line(line):
    split_line = line.split(']',1)
    if len(split_line)==1:
        return None
    else:
        split_line[0] = int(split_line[0].replace('[',''))
        split_line[1] = split_line[1].strip()    
    return (split_line[0],split_line[1])


def turn_stats(summary):
    
    lines = summary.split('\n')
    turn_results = []
    temp = []
    num_errors = 0

    for line in lines:

        if 'stop' in line:
            number_turn, parsed_line = parse_trace_line(line)
            temp = [pair.split('=')[1] for pair in parsed_line.split()]
            turn_results.append({
                'turn': int(number_turn),
                'stop': temp[0],
                'in': int(temp[1]),
                'out': int(temp[2]),
                'errors': num_errors 
            })
            num_errors = 0
        
        elif 'tool_result error' in line:
             num_errors=1

    return  turn_results


def first_error_turn(summary):
    num_errors=0
    turns = turn_stats(summary)

    for turn in turns:
        if turn['errors']!=0:
            num_errors+=1
    
    if num_errors==0:
        return None 
    return num_errors


def total_calls(summary):
    turns = summary.split('\n')

    for turn in turns:
        if 'total calls' in turn:
            turn_split = turn.split(' ')
            number_calls = turn_split[1].split('=')[1] 
            return int(number_calls)
    
    return 0


def grade_run(expected, actual, summary):
    
    if expected==None or actual==None:
        comparaison=False 
    else:
        expected = expected.lower().strip()
        actual = actual.lower().strip()
        comparaison= actual==expected

    return {'passed': comparaison,
        'calls':total_calls(summary),
        'first_bad_turn': first_error_turn(summary)
        }


def pass_rate(results):
    
    size = len(results)
    if size==0:
        return 0.0 

    true_passed = 0
    for result in results:
        if result['passed']==True:
            true_passed+=1
    
    return round(true_passed/size,2)
