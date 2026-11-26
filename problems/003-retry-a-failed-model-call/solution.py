def call_with_retry(fn, max_attempts=3, base_delay=1.0):
    """Call fn(), retrying transient failures with exponential backoff.

    Re-raise the last exception once max_attempts is exhausted.
    """
 
    for attempt in range(max_attempts):
        try:
            return fn()
        
        except (RateLimitError, TimeoutError, ServerError) as e:
            # last_raise= e
            if attempt==max_attempts-1:
                raise 
            sleep( base_delay * (2 ** attempt))
                

    # return last_raise
