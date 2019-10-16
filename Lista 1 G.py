entrada = int (input())

cem = entrada//100
resto1 = entrada%100

cinquenta = resto1//50
resto2 = resto1%50

vinte = resto2//20
resto3 = resto2%20

dez = resto3//10
resto4 = resto3%10

cinco = resto4//5
resto5 = resto4%5

dois = resto5//2
resto6 = resto5%2

um = resto6



print("%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00" %(cem, cinquenta, vinte, dez, cinco, dois, um))