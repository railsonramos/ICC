snake=input()
camel=""
for i in range(len(snake)):
    if i==0 and snake[i]!="_":
        camel+=snake[i].upper()
    if snake[i]=="_" and i<(len(snake)-1) and snake[i+1]!="_" :
        camel+=snake[i+1].upper()
    if snake[i-1]!="_" and i!=0 and snake[i]!="_":
        camel+=snake[i]
 
print(camel)
