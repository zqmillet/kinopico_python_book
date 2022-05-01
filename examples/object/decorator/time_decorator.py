from time import time

def print_time(function):
    def wrapper(*args, **kwargs):
        now = time()
        return_value = function(*args, **kwargs)
        print(f'consuming time {time() - now}s')
        return return_value
    return wrapper

@print_time
def add(x, y):
    return x + y

print(f'add(1, 2) = {add(1, 2)}')
print(f'add(3, 2) = {add(3, 2)}')
