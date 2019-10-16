def pares (n):
    if n == 0 or n == 1:
        return 0
    if n%2 == 0:
        print (n)
        return pares (n - 2)
    else:
        print (n-1)
        return pares (n-2)
 
n = int (input())
maior = n
pares (n)
 
