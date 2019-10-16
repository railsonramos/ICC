primeiro_numero = int (input())
 
 
 
stop = 0
 
maior = primeiro_numero
 
while stop < 9:
    entrada = int(input())
    stop += 1
 
    if entrada > maior:
        maior = entrada
 
print("%d" %maior)
if (maior % primeiro_numero) == 0:
    print ("%d" %primeiro_numero)
 
 
