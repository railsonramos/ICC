a = int (input())
def fibonacci (n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fatorial (n):
    if n==0 or n==1:
        return 1

    else:

        return n*fatorial(n-1)

print (fibonacci (a), fatorial(a), end = " ")

if fibonacci (a) % 2 == 0:
    print (fibonacci(a-1)