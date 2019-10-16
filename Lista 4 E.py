s1 = str(input())
s2 = str(input())
 
print(s1 + s2)
print(s1[::-1])
 
prefixo = False
if not s1 and s2:
    prefixo = True
 
elif len(s1) < len(s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            prefixo = True
        else:
            prefixo = False
            break
 
print(prefixo)
 
 
