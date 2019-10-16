#X = primiro valor
#Y = numero de números impares à ser contados


numero_de_linhas = int(input())
soma = 0
contador = 0
for i in range (numero_de_linhas):
    x, y = input().split()
    x, y = [int(x), int(y)]


    while contador < y:
        if (x % 2) != 0:
            contador += 1
            soma += x
        x += 1
    print (soma)

    if i == 0:
        maior = soma
        menor = soma
    if maior > soma:
        menor = soma
    if maior < soma:
        maior = soma

print ("%d" %maior)
print ("%d" %menor)
