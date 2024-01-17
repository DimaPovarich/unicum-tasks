import dis
from math import factorial
from math import sqrt
from math import pi
from math import e

def math_factorial(val):
    return (sqrt(2*pi*val))*(val**val/e**val)

print()

print(f'наша функция: {math_factorial(6)}')
print(f'math функция: {factorial(6)}')
print(f'ошибка: {factorial(6) - math_factorial(6)}')


def count_operations(code_line):
    instr = dis.get_instructions(code_line)
    count = 0
    for i in instr:
        if 'LOAD' in i.opname or 'STORE' in i.opname:
            # Другие типы операций можно добавить по аналогии
            count += 1
    return count
code = """
print(f'наша функция: {math_factorial(6)}')
"""
code1 = """
print(f'math функция: {factorial(6)}')
"""

operation_count = count_operations(code)
operation_count1 = count_operations(code1)
print('кол-во операций в нашей функции: ', operation_count)
print('кол-во операций в math функции: ', operation_count1)