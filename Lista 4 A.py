def retorno (x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    else:
        return 0
 
 
x = int(input())
y = int(input())
 
if retorno (x,y) == 1:
    print ("x e maior que y")
elif retorno (x,y) == -1:
    print ("x e menor que y ")
elif retorno (x,y) == 0:
    print ("x e igual a y")
