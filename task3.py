import math
import sys

try:
    a = float(input("Type a: "))
    b = float(input("Type b: "))
    c = float(input("Type c: "))
except:
    print('Invalid input format. Coefficients cant be string, bool and etc.')
    sys.exit()

output = f'Your quadratic equation: {a}x^2+{b}x+{c}=0' 
print (output.replace('+-', '-'))

D = b*b-4*a*c
print(f'Discriminant: {D}')

if D>0:
    print(f'x1 = {(-b+math.sqrt(D))/(2*a)} ')
    print(f'x2 = {(-b-math.sqrt(D))/(2*a)} ')
elif D==0:
    print(f'x1 = {-b/(2*a)} ')
elif D<0:
    print('No solutions')