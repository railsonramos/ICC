entrada  = int (input())

contador  = 0

somatorio = entrada

maior = entrada

while entrada != 0:
    contador = contador + 1
    entrada = int (input ())
    if entrada > maior and entrada != 0:
        maior = entrada
    somatorio = (somatorio + entrada)
    media = somatorio/contador

if contador == 0:
    media = 0

print ("%d" %contador)
print ("%d" %maior)
print ("%.2f" %media)