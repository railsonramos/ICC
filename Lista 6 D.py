n,p = input().split()
n,p = int(n), int(p)
 
lista = []
 
for i in range (n):
    if i == p:
        lista += ["p"]
    else:
        lista += ["b"]
 
for i in range (n):
    x,y = input().split()
    y = int(y)
    if lista [y] == "p":
        g = x
        del lista [y]
    else:
        del lista[y]
print (g)
 
