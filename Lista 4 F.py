a = 1
b = 1
 
 
def mmc(a, b):
    while a >= 0 and b >= 0:
        a, b = input().split()
        a, b = [int(a), int(b)]
        for i in range(1, 999999999999999):
            if b > 0 and a > 0:
                if i % a == 0 and i % b == 0:
                    print(i)
                    break
            if a == 0 and b > 0:
                print(0)
                break
            if b == 0 and a > 0:
                print(0)
                break
            if a == 0 and b == 0:
                print(0)
                break
            if b < 0 or (b == 0 and a < 0):
                break
            if a < 0 and b > 0:
                break
 
 
mmc(a, b)
 
