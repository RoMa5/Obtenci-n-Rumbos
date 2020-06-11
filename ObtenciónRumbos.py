import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
import csv
import math 

X=[]
Y=[]
Vertice = []

f = open('Coordenadas.csv', 'r')
if f.mode == "r":
    contenido = f.read()
    
with open ('Coordenadas.csv') as f:
    reader = csv.reader(f)
    print ('Los datos importados son: ')
    print('                           ')
    for row in reader:
        print(row)
    print('                           ')


with open ('Coordenadas.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        X.append(float(row['X']))
        Y.append(float(row['Y']))
        Vertice.append(float(row['Vertice']))
     
    x1 = (X[0])
    x2 = (X[1])
    x3 = (X[2])
    x4 = (X[3])

      
    y1 = (Y[0])
    y2 = (Y[1])
    y3 = (Y[2])
    y4 = (Y[3])

    
    v1 = (Vertice[0])
    v2 = (Vertice[1])
    v3 = (Vertice[2])
    v4 = (Vertice[3])

    
    r1 = ((x2-x1)/(y2-y1))
    r2 = ((x3-x2)/(y3-y2))
    r3 = ((x4-x3)/(y4-y3))
    r4 = ((x1-x4)/(y1-y4))
        
    tg1 = math.atan(r1)
    grados1 = math.degrees(tg1)

    tg2 = math.atan(r2)
    grados2 = math.degrees(tg2)

    tg3 = math.atan(r3)
    grados3 = math.degrees(tg3)

    tg4 = math.atan(r4)
    grados4 = math.degrees(tg4)

    
    
    if ((y2-y1)>0) and ((x2-x1)>0):
        print('El rumbo de',v1,'a',v2,'es',grados1,'NE')
    else:
        if ((y2-y1)>0) and ((x2-x1)<0):
             print('El rumbo de',v1,'a',v2,'es',grados1,'NW')
        else:
            if ((y2-y1)<0) and ((x2-x1)<0):
                print('El rumbo de',v1,'a',v2,'es',grados1,'SW')
            else:
                print('El rumbo de',v1,'a',v2,'es',grados1,'SE')

    
    if ((y3-y2)>0) and ((x3-x2)>0):
        print('El rumbo de',v2,'a',v3,'es',grados2,'NE')
    else:
        if ((y3-y2)>0) and ((x3-x2)<0):
             print('El rumbo de',v2,'a',v3,'es',grados2,'NW')
        else:
            if ((y3-y2)<0) and ((x3-x2)<0):
                print('El rumbo de',v2,'a',v3,'es',grados2,'SW')
            else:
                print('El rumbo de',v2,'a',v3,'es',grados2,'SE')

    
    if ((y4-y3)>0) and ((x4-x3)>0):
        print('El rumbo de',v3,'a',v4,'es',grados3,'NE')
    else:
        if ((y4-y3)>0) and ((x4-x3)<0):
             print('El rumbo de',v3,'a',v4,'es',grados3,'NW')
        else:
            if ((y4-y3)<0) and ((x4-x3)<0):
                print('El rumbo de',v3,'a',v4,'es',grados3,'SW')
            else:
                print('El rumbo de',v3,'a',v4,'es',grados3,'SE')

         
    
    if ((y1-y4)>0) and ((x1-x4)>0):
        print('El rumbo de',v4,'a',v1,'es',grados4,'NE')
    else:
        if ((y1-y4)>0) and ((x1-x4)<0):
             print('El rumbo de',v4,'a',v1,'es',grados4,'NW')
        else:
            if ((y1-y4)<0) and ((x1-x4)<0):
                print('El rumbo de',v4,'a',v1,'es',grados4,'SW')
            else:
                print('El rumbo de',v4,'a',v1,'es',grados4,'SE')

plt.plot(X,Y, Label='Poligono')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plano Catastral')
plt.legend()
plt.show()

