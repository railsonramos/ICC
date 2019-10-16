horas = int(input())

hora = horas//60
resto1 = horas%60

minuto = resto1//60
resto2 = resto1%60

segundo = resto2

print("%ih:%im:%is" %(hora, minuto, segundo))