import time
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        use = end-start
        print(func.__name__)
        print(use)

        return result
    return wrapper

@timer
def write(m):
    sum = 0
    for i in m :
        sum+=i

    return sum

m = [1,2,4,1,2,3,6,2]
print(write(m))

    