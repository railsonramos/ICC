n = int(input())
matriz=[]
for i in range(n):
    s = input().split()
    matriz.append(s)
 
x=0
while x<15:
    for j in range(len(matriz)):
        for y in range(len(matriz)):
            if matriz[j][y] == "o" and j < (len(matriz)-1) and matriz[j+1][y]==".":
                matriz[j][y],matriz[j+1][y] = ".","o"
    x+=1
    
for k in range(n):
    print(' '.join(matriz[k]),end="")
    print()
 
