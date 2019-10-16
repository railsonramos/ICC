def MDC (x, y):
    resto = None
    while resto != 0:
        resto = x % y
        x = y
        y = resto
    return x


a, b = input().split()
a, b = [int(a), int(b)]

print (MDC(a,b))