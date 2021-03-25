from functools import wraps
import time


# time wrapper
def gt(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        p_time = time.time()
        await func(*args, **kwargs)
        print(f"Time consumed: %.3f" % (time.time()-p_time))
    return wrapper
