def my_decorator(number):
    def wrapper(*x, **q):
        res = number(int(input('введите число: ')), int(input('введите второе число: ')))
        return res * 2
    return wrapper

@my_decorator
def number(num1, num2):
    return num1+num2

print(f'результат(программа их сложила и умножила на 2): {number()}')
