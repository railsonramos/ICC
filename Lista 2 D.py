a,b = input().split()
a, b = [int(a), int(b)]

if (0<=a<=100 and 0<=b<=100):
    if a-b == 0 or a-b == 1 or a-b == -1:
        print ("%i %i ok" %(a, b))
    else:
        print ("%i %i errados" %(a, b))