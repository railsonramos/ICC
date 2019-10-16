n = int (input())
a = int (input())

while (a != n):
    if a > n:
        print ("O número correto é menor.")
    elif a < n:
        print ("O número correto é maior.")
    a = int (input ())

print ("Parabéns! Você acertou.")