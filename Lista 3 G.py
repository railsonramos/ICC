entrada = int (input())
m = 0
primo = True

while primo:
    m = m + 1
    x = entrada *m+1

    for i in range (2, x):
        if (x % i) == 0:
            primo = False

print ("%d"%m)