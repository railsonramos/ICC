def soma (n):
    if n<0:
        return -1
    if n == 0 or n == 1:
        return 0
    else:
        if n%2 == 0:
            return  n- 2 + soma (n-2)
        else:
            return soma (n-1)
 
n = int (input())
print (soma(n))
 
