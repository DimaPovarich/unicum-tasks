class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def plus(self, num, num1):
        print(num + num1)
    def minus(self, num, num1):
        print(num - num1)
    def multiplie(self, num, num1):
        print(num * num1)
    def division(self, num, num1):
        try:
            print(num / num1)
        except ZeroDivisionError:
            print('Не дели на ноль!!')

class Figure_Calculator:
    def square(self, num):
        return num**2
    def triangle(self, h, num):
        return 0.5*h*num
    def sircle(self, r):
        return r**2*3.14

my_calculator = Calculator(int(input('first number: ')), int(input('second number: ')))
my_S_calculator = Figure_Calculator

my_calculator.plus(my_calculator.num1, my_calculator.num2)
my_calculator.minus(my_calculator.num1, my_calculator.num2)
my_calculator.multiplie(my_calculator.num1, my_calculator.num2)
my_calculator.division(my_calculator.num1, my_calculator.num2)

print(my_S_calculator.square(self= my_S_calculator, num=float(input('введите сторону квадрата: '))))
print(my_S_calculator.triangle(self = my_S_calculator, h = float(input('введите высоту треугольника от основания: ')), num=int(input('введите длину основания треугольника: '))))
print(my_S_calculator.sircle(self = my_S_calculator, r=float(input('введите радиус круга: '))))
