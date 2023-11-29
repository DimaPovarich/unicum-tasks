def my_decorator(multiply):
    def warapper(*args, **kwargs):
        print(f"Calling function {multiply.__name__} with args: {args} and kwargs: {kwargs}")
        result = multiply(*args,**kwargs)
        print(f"function {multiply.__name__} returned {result}.")
        return result
    return warapper

@my_decorator
def multiply(a,b):
    return a*b

print(multiply(2,2))