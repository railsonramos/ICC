n = int(input()) #numero de problemas a serem resolvidos
lista = []
tupla = ()
saida = ""
 
for i in range(n):
    problema, solucao, dificuldade = input().split()
    dificuldade = int(dificuldade)
    tupla = (dificuldade, solucao)
    lista.append(tupla)
    lista.sort()
    lista.reverse()
for j in range(len(lista)):
    saida += lista[j][1]
 
print(saida)    
 
