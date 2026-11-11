def is_retryable(error):
    error_value = getattr(error, 'status', None)
    if error_value == 429 or error_value == 529:
        return True
    else: 
        return False


def backoff_delay(attempt, base=0.5):
    return base * 2 ** attempt


def retry_after(headers):
    try:
        return int(headers.get('Retry-After',[]))
    
    except:
        return None


def call_with_retry(fn, attempts=4, base=0.5, sleep=time.sleep):

    for attempt in range(attempts):
        try:
            return fn()
        
        except APIError as e: 
            if attempt == attempts - 1 or not is_retryable(e):
                raise
            
            # 3. Otherwise, wait the calculated delay before the loop repeats
            sleep(backoff_delay(attempt, base))
