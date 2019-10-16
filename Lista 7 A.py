n = int(input())
dicionario = {}
 
for i in range(n):
    chave, valor = input().split()
    dicionario.update({chave:valor})
 
string = input()
saida = ""
 
for palavra in string.split():
    if palavra in dicionario.keys():
        saida += dicionario[palavra] + " "
        
saida = saida[:-1]
if len (saida) == 0:
    print("Tudo bem!")
else:
    print(saida)
