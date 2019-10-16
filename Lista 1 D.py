x1, y1 = input().split()
x2, y2 = input().split()
complexo = complex(input())

x1,y1,x2,y2 = [float(x1), float(y1), float(x2), float(y2)]

distancia  = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

z = ((complexo.imag)**2 + (complexo.real)**2)**(1/2)


print ("%.4f\n%.4f" %(distancia, z))

