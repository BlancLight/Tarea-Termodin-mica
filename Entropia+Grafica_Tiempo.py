#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:44:27 2020

@autores: Jesús Andrey Salazar Araya, Angello Marconi Crawford Clark
"""
#Librerías utilizadas
import numpy as np
import math
import matplotlib.pyplot as plt 

lista_S = []#Se crea una lista que va a albergar cada valor de entropía para cada paso
lista_estados = []#Se crea una lista que va a albergar cada valor de paso o tiempo

def entropia():#Esta función calcula la entropía de cada estado o bien de cada tiempo y devuelve el valor de entropía para cada tiempo
    z=np.load('Estado_Crema'+ str(t)+'.npy')#Procede a llamar a la matriz de cada estado/tiempo
    entropiaestado=0#Contador entropia de estado

    for i in range(10):#Ciclo for para recorrer la matriz 100x100 en filas de celdas 10x10, tiene que recorrer 10 filas de celdas 10x10
        for j in range(10): #Ciclo for para recorrer la matriz 100x100 en columnas de celdas 10x10, tiene que recorrer 10 columnas de celdas 10x10
            f = z[10*i:10*i+10,10*j:10*j+10]#Permite cortar la matriz para poder dividirla en celdas de 10x10
            numero=0#Contador de la cantidad de unos por celda 10x10
            for u in range(len(f)):#Ciclo for que recorre las filas de las celdas 10x10
                for v in range(len(f[0])):#Ciclo for que recorre las columnas de las celdas 10x10
                
                    if f[u][v]==1:#Si la celda 10x10 en la posición indicada es un uno procede a hacer lo siguiente:
                        numero+=1#Si es un uno aumenta el contador numero en 1 unidad
            pi=numero/100#Procede a hacer el cálculo de probabilidad (cantidad de unos que hay en la celda analizada 10x10 / 100)
            if pi==0:#Condición de si la probabilidad es 0
                S=0#La entropía es 0, la condición se hace para no calcular el logaritmo natural de 0 que da error
            else:#De lo contrario
                S=-(pi)*math.log(pi)#Calcula la probabilidad con la formulación de Gibbs, esta S representa la entropía por celda 10x10
                                      
            entropiaestado += S#Este contador suma todas las entropías de las celdas 10x10 para calcular la entropia de
            
    return entropiaestado#valor que devuelve la función entropia(t)
                    

k=20000#Número de pasos que debe correr la simulación o t = 20000
for t in range(k):#Ciclo for para recorrer el tiempo = k
    lista_S.append(entropia())#Lo que hace es agregar el valor de entropia en la lista de entropia
    
for t in range(k):#Ciclo for para recorrer el tiempo = k
    lista_estados.append(t)#Lo que hace es agregar el valor de tiempo en la lista_estados
    
plt.plot(lista_estados,lista_S,color="blue")#Función que permite graficar los valores de las listas creadas con los parámetros x,y,color)
plt.xlabel('Tiempo(pasos)')#Nombre del eje x
plt.ylabel('entropia')#Nombre del eje y
plt.title('Evolucion de la entropia del sistema')#Título de la gráfica
plt.show()#Función que muestra la gráfica de variación de entropía en el tiempo


