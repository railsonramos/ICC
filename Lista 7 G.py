n = int(input())
jogadas = []
 
for i in range(n):
    x, y = input().split()
    y = int(y)
    jogadas.append((x, y))
 
jogadas2 = jogadas[n - 1][1]
 
while jogadas[jogadas2 - 1][1] != n:
    jogadas2 = jogadas[jogadas2-1][1]
 
print(jogadas[jogadas2 - 1][0])
 
