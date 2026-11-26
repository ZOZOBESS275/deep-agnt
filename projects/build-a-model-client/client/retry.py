def is_retryable(error):
    
    try:
        if error.status==429 or error.status==529:
            return True
        else:
            return False

    except:
        return False


def backoff_delay(attempt, base=0.5, cap=8.0):
    delay = base * 2 ** attempt
    if delay > cap:
        return cap
    return delay


import time


def call_with_retry(fn, attempts=4, base=0.5, sleep=time.sleep):
    
    for attempt in range(attempts):
        try:
            return fn()
    
        except Exception as e:
            if attempt == attempts-1 or not is_retryable(e):
                raise
            
            sleep(backoff_delay(attempt,base))
