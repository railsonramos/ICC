a = int (input())
b = int (input())
c = int (input())

maior = 999999999999999999999
menor = -999999999999999999999

if b > a:
    maior = b
    b = a
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
