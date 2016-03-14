# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:02:44 2016

@author: Misael Pacheco
"""
#librería para leer imágenes
import matplotlib.image as imgs
#librería utilizada para abrir archivos, la cual se utilizar para abrir carpetas el dataSet
import os
#librería para crear el archivo csv sonde de almacenaran las caracteristicas de las imágenes obenidas
import csv

#Declaramos dos variables globales para almacenar el valor de filas y columnas de una imagen

#La Variable "alto" contiene las columnas de la imagen
alto=0
#La variable "ancho# contiene las filas de la imagen
ancho=0
#Nombre: primerCaracteristica
#Descripción: obtiene la relación del número de 1's entre los píxeles de la imagen, es decir, relación = #1's/(#filas)(#columnas) 
#Parametros entrada: Variable "img" la cual contiene la imagene de la que se obtendra la caracteristica, 
#Parametros de salida: Variable con el nombre "ab" el cual regresa el valor de la relación de #columas/#filas
def primerCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    #Obetenemos el número de columnas de la imagen seleccionada
    alto=len(img)
    #Dividimos el tamaño total de la imagen, "im", entre el número de columas
    ancho=int(tam/alto)
    #variables con las que se va a recorrer el for    
    contadorDeUnos = 0
    #este ciclo nos sirve para la cantidad de unos que existen en la imagen
    for a in range(alto):
        for b in range(ancho):
            #almacenamos en la variable num los datos de la matriz
            dato = (int(img[a][b]))
            #comparamos la variable dato si es equivalente a un 1            
            if dato!=1:
                #contador de los unos que encuentra
                contadorDeUnos = contadorDeUnos+1
    #retornamos la varible contadorUnos para ser almacenada en la matriz
    return contadorDeUnos/(alto*ancho)
    

#Nombre: segundaCaracteristica
#Descripión: Relación entre número de colmnas y numero de filas
#Parametros entrada: Variable "img" la cual contiene la imagene de la que se obtendra la caracteristica, 
#Parametros de salida: Variable con el nombre "r" el cual regresa el valor de la relación de entre el #filas y #columnas 
def segundaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    #Obetenemos el número de columnas de la imagen seleccionada    
    alto=len(img)
    #Obetenemos el número de las filas de la imagen seleccionada    
    ancho=int(tam/alto)
    #obtenemos un promedio de filas y columnas que almacenamos
    #en la variable prom    
    prom = ancho/alto
    #retornamos prom para ser almacenado en la matriz
    return prom

#Nombre: tercerCaracteristica
#descripcion: obtiene la relacion del numero de 1´s entre los pixeles de la fila intermedia de la imagen
#Parametros entrada: Variable "img" la cual contiene la imagene de la que se obtendra la caracteristica, 
#Parametros de salida: Variable con el nombre "contadorDeUnos" el cual regresa el valor de la relación de entre el #filas y #columnas 
def tercerCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila que se encuentra en medio de la matriz de la imagen
    filaIntermedia = int(ancho/2)
    #declaramos la variable que contara los 1´s de la fila intermedia
    contadorDeUnos = 0
    #ciclo que nos ayuda a recorrer dicha fila
    for al in range(alto):
        #declaramos la variable que encuntra a los 1´s en la fila
        dato = (int(img[al][filaIntermedia]))
        #condicion para saber si es un 1 el dato de la fila
        if dato == 1:
            #contamos los 1´s que existen en la fila intermedia
            contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)
    
#Nombre: cuartaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def cuartaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila que se encuentra en 1/4 de la matriz de la imagen
    filaUnCuarto= int(ancho/4)
    #declaramos la variable que contara los 1´s de la fila 1/4
    contadorDeUnos = 0
    #ciclo que nos ayuda a recorrer dicha fila
    for al in range(alto):
        #declaramos la variable que encuentra a los 1´s en la fila
        dato = (int(img[al][filaUnCuarto]))
        #condicion para saber si es un 1 el dato de la fila
        if dato == 1:
            #contamos los 1´s que existen en la fila intermedia
           contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#Nombre: quintaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def quintaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila que se encuentra a 3/4 de la matriz de la imagen
    filaTresCuartos = int((int(ancho/4))*3)
    #declaramos la variable que contara los 1´s de la fila 3/4
    contadorDeUnos = 0
    #ciclo que nos ayuda a recorrer dicha fila
    for al in range(alto):
        #declaramos la variable que encuentra a los 1´s en la fila
        dato = (int(img[al][filaTresCuartos]))
        #condicion para saber si es un 1 el dato de la fila
        if dato == 1:
            #contamos los 1´s que existen en la fila 3/4
            contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)
       
#Nombre: sextaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def sextaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la columna intermedia de la matriz de la imagen
    colItermedia = int(alto/2)
    #declaramos la variable que contara los 1´s de la columna intermedia
    contadorDeUnos = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columas de la matriz
        for col in range(ancho):
            #condicion para saber si las columna es la del 1/4
            if fil == colItermedia:
                #alamacenamos el dato que obtenemos de la matriz
                dato = (int(img[colItermedia][col]))
                #condicion para saber si es un 1 el dato de la columna
                if dato == 1:
                    #contamos los 1´s que existen en la columna intermedia
                    contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#Nombre: septimaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def septimaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la columna que se encuentra en 1/4 de la matriz de la imagen
    columnaUnCuarto = int(alto/4)
    #declaramos la variable que contara los 1´s de la columna 1/4
    contadorDeUnos = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion que compara la columna con la columna 1/4
            if fil == columnaUnCuarto:
                #declaramos la variable que encuentra a los 1´s en la columna
                dato = (int(img[columnaUnCuarto][col]))
                #condicion para saber si es un 1 el dato de la columna
                if dato == 1:
                    #contamos los 1´s que existen en la columna 1/4
                    contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)


#Nombre: octavaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def octavaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila que se encuentra a 3/4 de la matriz de la imagen
    colTresCuartos = int((int(alto/4))*3)
    #declaramos la variable que contara los 1´s de la columna 3/4
    contadorDeUnos = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion que compara la columna con la columna 3/4
            if fil == colTresCuartos:
                #declaramos la variable que encuentra a los 1´s en la columna
                dato = (int(img[fil][col]))
                #condicion para saber si es un 1 el dato de la columna
                if dato == 1:
                    #contamos los 1´s que existen en la columna 1/4
                    contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)


#Nombre: novenaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def novenaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila intermedia de la matriz de la imagen
    columnaIntermedia = int(ancho/2)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo que recorre la matriz para obtener los cortes
    for fil in range(alto):
        #obtenemos el dato de la matriz
        dato = (int(img[fil][columnaIntermedia]))
        #comparamos el dato con el corte
        if dato!=corte:
            #contamos el corte que se produjo
            contadorDeCortes = contadorDeCortes+1
            #corte = (int(img[fil][columnaIntermedia]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)


#Nombre: decimaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def decimaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila que se encuentra en 1/4 de la matriz de la imagen
    filaUnCuarto = int(ancho/4)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo que recorre la matriz para obtener los cortes
    for fil in range(alto):
        #obtenemos el dato de la matriz
        dato = (int(img[fil][filaUnCuarto]))
        #comparamos el dato con el corte
        if dato!=corte:
            #contamos el corte que se produjo
            contadorDeCortes = contadorDeCortes+1
            #corte=(int(img[fil][filaUnCuarto]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#Nombre: onceavaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def onceavaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la columna que se encuentra a 3/4 de la matriz de la imagen
    col = int((int(ancho/4))*3)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo que recorre la matriz para obtener los cortes
    for al in range(alto):
        #obtenemos el dato de la matriz
        dato = (int(img[al][col]))
        #comparamos el dato con el corte
        if dato!=corte:
            #contamos el corte que se produjo
            contadorDeCortes = contadorDeCortes+1
            #corte = (int(img[al][col]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#Nombre: doceavaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def doceavaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila intermedia de la matriz de la imagen
    columaIntermedia = int(alto/2)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo para recorrer las filas de la matriz
    for an in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for an2 in range(ancho):
            #condicion para encontrar la columna intermedia
            if an==columaIntermedia:
                #obtenemos el dato de la matriz
                dato = (int(img[columaIntermedia][an2]))
                #comparamos el dato con el corte
                if dato!=corte:
                    #contamos el corte que se produjo
                    contadorDeCortes = contadorDeCortes+1
                    #corte = (int(img[columaIntermedia][an2]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#Nombre: treceavaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def treceavaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la fila que se encuentra en 1/4 de la matriz de la imagen
    columnaUnCuarto = int(alto/4)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion para encontrar la columna 1/4
            if fil == columnaUnCuarto:
                #obtenemos el dato de la matriz
                dato = (int(img[columnaUnCuarto][col]))
                #comparamos el dato con el corte
                if dato!=corte:
                    #contamos el corte que se produjo
                    contadorDeCortes = contadorDeCortes+1
                    #corte = (int(img[al][an2]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#Nombre: catorceavaCaracteristica
#Descrición: 
#Parametros entrada:
#Parametros de salida: 
def catorceavaCaracteristica(img):
    #Obtenemos el tamaño total de la imagen        
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    #obtenemos la columna que se encuentra a 3/4 de la matriz de la imagen
    columnaTresCuartos = int((int(alto/4))*3)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion para encontrar la columna 3/4
            if fil == columnaTresCuartos:
                #obtenemos el dato de la matriz
                dato = (int(img[columnaTresCuartos][col]))
                #comparamos el dato con el corte
                if dato!=corte:
                    #contamos el corte que se produjo
                    contadorDeCortes = contadorDeCortes+1
                    #corte = (int(img[columnaTresCuartos][col]))
    #retorna el numero de cortes de la imagen (matriz)   
    return contadorDeCortes/(alto*ancho)

#----------------------------------------------------Main------------------------------------
#Creamos la matriz donde se alamacenara los datos de las carracteristicas
print("obteniendo carracteristicas, por favor espere un momento")
matriz = [] 
#Iniciamos el ciclo for para llenarla con 0
for i in range(2369):
    matriz.append([0]*15)
#Colocamos el nombre de la carpeta donde se encuentran las imagenes
rootDir = 'DatosPrueba'
#Creamos una variable para concatenar la ruta de los archivos
name=''
#Inicializamos x en 0 que controlara las filas
x=0
#Inicializamos y en 0 que controlara las columnas
y=0
#Iniciamos el ciclo for en el cual ingresaremos a cada carpeta de la carpeta "DatosPrueba"
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Directorio encontrado: %s' % dirName)
    #Iniciamos el ciclo for en el cual ingresaremos a cada archivo de la carpeta de imagenes
    for fname in fileList:
        #Concatenamos la dirección de los archivos         
        name=dirName+"/"+fname
        #en la variable img se almacvenara una imagen
        img = imgs.imread(name)
        
        #Mandamos a llamar la función primeracarracteristica la cual el return se almacenara en la matriz con la posición [x][y]
        matriz[x][y]=primerCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=segundaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=tercerCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=cuartaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=quintaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=sextaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=septimaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=octavaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=novenaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=decimaCaracteristica(img)
        #con esta linea avanzamos entre las columnas de la matriz
        y=y+1
        matriz[x][y]=onceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=doceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=treceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=catorceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=name[12]
        #incrementamos x para saltar de fila
        x = x+1
        #volvemos a cero y para volver a recorrer las columnas de la matriz
        y = 0   
        
#---------------------------------------------------------------------------
#Generacón del dataSet de la aplicación (Archivo csv)
#---------------------------------------------------------------------------
#pasamos los datos de la matriz a la variable datosMatriz
#creamos el documento en donde escribiremos los datos 
archivo = open('dataSet.csv','w',newline='')
#mandamos a escribir los datos como parametro de la libreria csv
escritura = csv.writer(archivo)
#escribimos en el documento las celdas con los nombres (titulos de propiedades)
escritura.writerow(["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","Clase"])
#finalmente escribimos la matriz de datos en el documento csv
print("Creando dataset, por favor espere un momento")
escritura.writerows(matriz)
#eliminamos la salida del documento
del escritura
#cerramos el archivo que escribimos con los datos
print("Dataset ha sido creado con exito")
archivo.close()

