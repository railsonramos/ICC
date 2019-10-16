n = int(input())
tupla = ()
 
 
for i in range(n):
    s , t1, t2, t3, t4 = input().split()
    tupla += (s, t1, t2, t3, t4)
 
pesquisa = input().split()
 
for i in range(0, len(tupla), 5):
    for j in range(i+1, i+5):
        if tupla[j] in pesquisa:
            print(tupla[i])
            break
