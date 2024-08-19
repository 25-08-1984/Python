# Calcular as raízes de uma equação do segundo grau
import math
import cmath

#Entrada dos dados

a= float(input('a:'))
b= float(input('b:'))
c= float(input('c:'))
if a ==0:
    print('Não é uma equação do segundo grau!!!')
else:
    delta = b**2-4*a*c
    if delta < 0:# Raízes complexas
        x1=(-b + cmath.sqrt(delta/(2*a)))
        x2 = (-b + cmath.sqrt(delta / (2 * a)))
        print("Raízes complexas")