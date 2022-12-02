import math
import sys
from cmath import sqrt as complex_sqrt

try:
    a = input("Type a: ")
    b = input("Type b: ")
    c = input("Type c: ")

    if 'j' in a:
        a = complex(a)
    else:
        a = float(a)

    if 'j' in b:
        b = complex(b)
    else:
        b = float(b)

    if 'j' in c:
        c = complex(c)
    else:
        c = float(c)
except: 
    print('Invalid input format. Coefficients cant be string, bool and etc.')
    sys.exit()

D = b*b-4*a*c
print(f'Discriminant: {D}')
    
if 'j' in str(D):
    print(f'x1 = {(-b+complex_sqrt(D))/(2*a)} ')
    print(f'x2 = {(-b-complex_sqrt(D))/(2*a)} ')
else:
    if D>0:
        print(f'x1 = {(-b+math.sqrt(D))/(2*a)} ')
        print(f'x2 = {(-b-math.sqrt(D))/(2*a)} ')
    elif D==0:
        print(f'x1 = {-b/(2*a)} ')
    elif D<0:
        print(f'x1 = {(-b+complex_sqrt(D))/(2*a)} ')
        print(f'x2 = {(-b-complex_sqrt(D))/(2*a)} ')
