h1, m1, h2, m2 = input().split()
h1, m1, h2, m2 = [int(h1), int(m1), int(h2), int(m2)]

horas1 = (h1 * 60) + m1

horas2 = (h2 * 60) + m2

diferenca2 = horas2 - horas1

if horas1==horas2:
    print("O jogo durou 24 hora(s) e 0 minuto(s)")

if horas1>horas2:
    horas = (diferenca2//60) + 24
    minutos = diferenca2%60
    print ("O jogo durou %i hora(s) e %i minuto(s)" %(horas, minutos))

if h1<h2:
    horas = diferenca2//60
    minutos = diferenca2%60
    print("O jogo durou %i hora(s) e %i minuto(s)" %(horas, minutos))