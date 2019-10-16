import string
 
texto = input()
trd = ""
texto = texto.lower()
dic = {}
freq = []
palavras = []
 
for letra in texto:
    if letra in string.ascii_lowercase or letra in " ’-":
        trd += letra
 
trd = trd.split()
 
for palavra in trd:
    if palavra.capitalize() in dic.keys():
        dic.update({palavra.capitalize():dic[palavra.capitalize()]+1})
    else:
        dic.update({palavra.capitalize():1})
 
for i in sorted(dic.values()):
    if i not in freq:
        freq.append(i)
 
for palavra in trd:
    if palavra not in palavras:
        palavras.append(palavra)
 
freq= freq[::-1]
 
for i in freq:
    for palavra in palavras:
        if dic[palavra.capitalize()] == i:
            print(palavra.capitalize(), dic[palavra.capitalize()])
 
