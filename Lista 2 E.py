m,d = input().split()
m,d = [int(m), int(d)]

if 1<=m<=12 and 1<=d<=7:
    if (m== 1 or m==3 or m==5 or m == 7 or m ==8 or m == 10 or m ==12) and (d==7 or d==6):
        print ("6")
    elif (m== 1 or m==3 or m==5 or m == 7 or m ==8 or m == 10 or m ==12) and (d==1 or d==2 or d==3 or d==4 or d==5):
        print ("5")
    elif m == 2 and d==1:
        print ("4")
    elif (m == 2) and  (d==2 or d==3 or d==4 or d==5 or d==6 or d==7):
        print ("5")
    elif (m == 4 or m == 6 or m== 9 or m == 11) and (d==7):
        print ("6")
    elif (m == 4 or m == 6 or m== 9 or m == 11) and (d == 1 or d==2 or d==3 or d==4 or d==5 or d==6):
        print ("5")