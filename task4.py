import math
from cmath import sqrt as complex_sqrt

def isComplexorFloat(value):
    """
    Определяет комплексное ли число
    Параметры:
    val -- проверяемое число
    Возвращает 
    val -- число приведенное к классу complex или float
    """
    if 'j' in value:
        return complex(value)
    else:
        return float(value)

while True:
    try:
        a = input("Type a: ")
        b = input("Type b: ")
        c = input("Type c: ")

        a = isComplexorFloat(a)
        b = isComplexorFloat(b)
        c = isComplexorFloat(c)
    except: 
        print('Invalid input format. Coefficients cant be string, bool and etc. Try again.')
        temp = input('Type "0" for exit. Else continue.')
        if temp == '0':
            break
        else: continue

    D = b*b - 4*a*c
    print(f'Discriminant: {D}')
        
    if 'j' in str(D):
        print(f'x1 = {(-b + complex_sqrt(D))/(2*a)} ')
        print(f'x2 = {(-b - complex_sqrt(D))/(2*a)} ')
    else:
        if D>0:
            print(f'x1 = {(-b + math.sqrt(D))/(2*a)} ')
            print(f'x2 = {(-b - math.sqrt(D))/(2*a)} ')
        elif D==0:
            print(f'x1 = {-b/(2*a)} ')
        elif D<0:
            print(f'x1 = {(-b + complex_sqrt(D))/(2*a)} ')
            print(f'x2 = {(-b - complex_sqrt(D))/(2*a)} ')
    break