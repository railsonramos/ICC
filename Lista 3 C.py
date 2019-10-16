#a = primeriro numero
#n = numero de algarismos

t = int(input())
for i in range (0, t):

    a,n = input().split ()
    a,n = [int(a), int(n)]

    soma = 0


    for j in range (a, a+n):
        print("%d" %j, end =" ")
        soma += j

    print("\n%d" %soma)

