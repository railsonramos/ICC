a = float (input())
b = float (input())
c = float (input())

maior = a
if b>maior:
    maior = b
    b = a
    a = maior
if c>maior :
    maior = c
    c=a
    a = maior


if a >= b + c:
    print ("NAO FORMA TRIANGULO")
elif a**2 == (b**2 + c**2):
    print ("TRIANGULO RETANGULO")
elif a == b == c:
    print ("TRIANGULO EQUILATERO")
elif   b==c or b==a or c==a:
    print ("TRIANGULO ISOSCELES")
else:
    print ("TRIANGULO ACUTANGULO OU OBTUSANGULO")
