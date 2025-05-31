import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

def speed_calc_decorator(func):
    def wrapper():
        func()
        print(f"{func.__name__} runtime = {time.time() - current_time} second(s)")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    
fast_function()
slow_function()