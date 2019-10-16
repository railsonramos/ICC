n = int(input())
brinquedos =[x for x in input().split()]
listaAntiga = brinquedos[:]
for i in range(5):
    brinquedo, direcao, deslocamento = input().split()
    deslocamento = int(deslocamento)
    indice = brinquedos.index(brinquedo)
    for j in range(deslocamento):
        if direcao =="D" and indice<len(brinquedos)-1:
            brinquedos[indice], brinquedos[indice+1]= brinquedos[indice+1],brinquedos[indice]
        indice = brinquedos.index(brinquedo)
        if direcao== "E" and indice>0:
            brinquedos[indice], brinquedos[indice-1]= brinquedos[indice-1], brinquedos[indice]
            indice = brinquedos.index(brinquedo)
contador =0
for i in range(len(brinquedos)):
    if( brinquedos[i]!=listaAntiga[i]):
        contador+=1
print(contador)
