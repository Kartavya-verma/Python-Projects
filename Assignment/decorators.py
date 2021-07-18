def decorator(func):
    def wrapper(*args,**kwargs):
        print("This is wrapper class ")
        return(func(*args,**kwargs))
    return wrapper


@decorator
def fun(a,b):
    return a+b

print(fun(1,2))