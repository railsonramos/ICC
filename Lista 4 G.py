def soma (x):
    if (x<0):
        return -1
    if (x==0 or x==1):
        return 0
    else:
        if x%2 ==0:
            print ("%d^2=%d" %(x,x**2))
            return soma (x-2)
        else:
            return soma (x-1)
x = 1
while x != 0:
    x = int (input())
    soma(x)
