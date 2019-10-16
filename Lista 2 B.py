massa = float (input())
altura = float (input())

IMC = massa/altura**2

massa_ideal = ((altura)**2) * 24.9

massa_peder = massa - massa_ideal

if IMC < 18.5:
    print("%.2f" %IMC)
    print ("Baixo peso")
elif IMC > 18.5 and IMC < 24.9:
    print("%.2f" % IMC)
    print ("Peso normal")
elif IMC > 24.9 and IMC < 29.9:
    print("%.2f" % IMC)
    print ("Sobrepeso")
elif IMC > 29.9 and IMC < 34.9:
    print("%.2f" % IMC)
    print ("Obesidade Grau I")
elif IMC > 34.9 and IMC < 39.9:
    print("%.2f" % IMC)
    print ("Obsesidade Grau II")
elif IMC > 39.9:
    print("%.2f" % IMC)
    print ("Obesidade Grau III")

if massa_peder > 0:
    print ("%.2f" %massa_peder)
