# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:34:08 2020

@author: Jesus Andrey Salazar Araya, Angello Marconi Crawford Clark
"""

#Librerías utilizadas
import numpy as np
import random
from matplotlib import pyplot as plt
#Creamos un arreglo  100X100 y luego a traves de un ciclo 'for'  agregamos los unos en el centro
l=np.zeros((100,100))
Arrayl=np.array(l, dtype=np.int64)
for i in range(44,54):
          for j in range(44, 54):
                Arrayl[i][j]=1
#Definimos dos constantes que van a ser las filas'row' y las colummnas'columns'
row=len(Arrayl)
columns = len(Arrayl[0])
#Definimos la función que nos va a generar el camino aleatorio 'Random Walk' y además nos guarda cada arreglo de la matriz
#'t' representa en tiempo o cantidad de pasos que queremos
def Ranpath(Arrayl,t):
                for k in range(t): 
                    np.save("Estado_Crema_"+str(k),Arrayl) #Guardar la matriz la cantidad de veces que iteramos
                    for a in range(row):
                        for b in range(columns):
                            if Arrayl[a][b]!=0:  #Para este punto lo que se hizo en el ciclo 'for'  anterior fue que me recorriera cada celda de la matriz 
                               paso=random.randint(0,3) #Si en la celda el detecta un '1' pues me genere un número aleatorio entre 0 y 3, de forma que tenemo 4 posibilidades [0,1,2,3]
                               if b+1<=columns-1: #Revisa que el elemento se encuentre dentro de los margen de las columnas y por lo tanto no corrernos a una celda inexistente
                                 if Arrayl[a][b+1]==0:#La función pregunta por el vecino de arriba de la celda en la que se encuentra, en los otros 'if' dentro del mismo indent  pregunta por los otros 
                                             if paso==0:#Acá entra el factor aleatorio establecido anteriormente
                                                 Arrayl[a][b]=0 #Si se cumple el paso anterior pues el valor de la celda actual cerá '0' 
                                                 Arrayl[a][b+1]=Arrayl[a][b+1]+1 #Luego de cambiar el valor de la celda actual, la celda que en este caso es la superior cambiará su valor a '1'
                               if b-1>=0: #Revisa margen de comlumna
                                 if Arrayl[a][b-1]==0:
                                             if paso==1:
                                                 Arrayl[a][b]=0
                                                 Arrayl[a][b-1]=Arrayl[a][b-1]+1 #Si se cumple lo anterior bajemos una celda
                               if a-1>=0: #Revisa margen de fila
                                 if Arrayl[a-1][b]==0:
                                             if paso==2:
                                                 Arrayl[a][b]=0
                                                 Arrayl[a-1][b]=Arrayl[a-1][b]+1 #Si se cumple lo anterior se mueve una celda a la izquierda
                               if a+1<=row-1: #Revisa margen de fila
                                 if Arrayl[a+1][b]==0:
                                             if paso==3:
                                                 Arrayl[a][b]=0
                                                 Arrayl[a+1][b]=Arrayl[a+1][b]+1 #Si se cumple lo anterior se mueve una celda a la derecha
                return Arrayl #Acá pedimos que nos devuelva la matriz para que vuelva a iterar y repita el ciclo hasta el 't' deseado
                                 
P=Ranpath(Arrayl,t) #Acá llamamos a la función y entonces P será el último arreglo de la matriz, se necesita sustituir t por un valor (ej:t=100)
for q in range(row):
    for w in range(columns):
         if Arrayl[q][w]!=0: #Con esta condición hacemos que dibuje los unos que se encuentran dentro de la matrzi
           plt.scatter([q],[w],2,color='b') #Finalmente, acá le decimos que la grafique

#En este punto simplemente le damos el formato a la impresión de los datos
plt.xlim(0,100) #Límite de la gráfica en el eje X
plt.ylim(0,100) #Límite de la gráfica en el eje Y
plt.xlabel('x') #Eje X
plt.ylabel('y') #Eje Y
plt.title('Cremas de café (t = t)') #Cambiar t por uno deseado (ej: t=20000)
plt.show() 