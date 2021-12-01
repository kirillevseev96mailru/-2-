from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)
    return wrapper

@decorator
def function(*args):
    return list(map(lambda x: x ** 3, args))


a = function(5, 3)
print(a)
