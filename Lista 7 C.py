n = int(input())
lista = [0, 0, 0, 0]
lista2 = lista[:]
#lista = [N, S, L, O]
 
for i in range(n):
    direcao, blocos = input().split()
    blocos = int(blocos)
    if direcao == "N":
        lista[0] += blocos
    if direcao == "S":
        lista[1] += blocos
    if direcao == "L":
        lista[2] += blocos
    if direcao == "O":
        lista[3] += blocos
 
deltaY = lista[0] - lista[1]
if deltaY >= 0:
    lista2[1] = deltaY
else:
    lista2[0] = -deltaY
 
deltaX = lista[2] - lista[3]
if deltaX >= 0:
    lista2[3] = deltaX
else:
    lista2[2] = -deltaX
 
 
print(lista2[0], lista2[1], lista2[2], lista2[3])
 
