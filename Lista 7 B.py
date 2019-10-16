n = int(input())
relacao = {}
lista = []
 
for i in range(n):
    dados = input().split()
    nome = dados[0].upper()
    lanche = " ".join(dados[1:])
    relacao.update({nome:lanche})
 
for chave in relacao.keys():
    lista += [chave]
    
lista.sort()
 
print(len(relacao))
 
for elemento in lista:
    print(relacao[elemento])
 
 
