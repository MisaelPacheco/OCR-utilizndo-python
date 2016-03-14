# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:02:44 2016

@author: Misael Pacheco
"""
#libreria que permite abrir imagenes
import matplotlib.image as mpimg
from PIL import Image
import math
import csv

#matriz temporal donde se almacenaran las propiedades de las imagenes
matriz = []
#se declr la variable que contendra el conteo de los vecinos del 0 al 9
contadorCero = 0
contadorUno = 0
contadorDos = 0
contadorTres = 0
contadorCuatro = 0
contadorCinco = 0
contadorSeis = 0
contadorSiete = 0
contadorOcho = 0
contadorNueve = 0
x = 0
y = 0
contadorClase = 0
#este ciclo llena la matriz con ceros
for i in range(2369):
    #llenamos la matriz con ceros y creamos las columnas
    matriz.append([0.0]*15)

#Obtenemos las carracteristicas de la nueva imagen a comparar utilizando las mismas funciones que en el codido "ORC.py"
def primerCaracteristica(img,alto,ancho):
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
def segundaCaracteristica(img,alto,ancho):
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
def tercerCaracteristica(img,alto,ancho):
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
def cuartaCaracteristica(img,alto,ancho):
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
def quintaCaracteristica(img,alto,ancho):
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
def sextaCaracteristica(img,alto,ancho):
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
def septimaCaracteristica(img,alto,ancho):
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
def octavaCaracteristica(img,alto,ancho):
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
def novenaCaracteristica(img,alto,ancho):
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
def decimaCaracteristica(img,alto,ancho):
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
def onceavaCaracteristica(img,alto,ancho):
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
def doceavaCaracteristica(img,alto,ancho):
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
def treceavaCaracteristica(img,alto,ancho):
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
def catorceavaCaracteristica(img,alto,ancho):
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

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def kNN(img, numVeci):
   #leemos la imagen de entrada 
    imgc = mpimg.imread(img)
    #creamos la matriz de para almacenar los datos de la imagen de entrada
    mat = []
    #matriz para los vecinos mas cercanos
    knn = []
    #contador para recorrer las columnas
    cont = 0

    #obtenemos informacion de la imagen
    imgCoFi = Image.open(img)
    #obtenemos filas y columnas de la imagen
    (fil,col) = imgCoFi.size
    #ciclo que recorre la matriz
    for x in range(2369+1):
        #llenamos la matriz con ''
        mat.append(['']*15)
    #ciclo que recorre la matriz de knn 
    for x in range(2369):
        #llenamos la matriz con '' para almacenar la distancia y la clase
        knn.append(['']*3)
    #leemos el archivo del dataSet
    reader = csv.reader(open('dataSet.csv'))
    #ciclo que llena la matriz con los datos del dataSet
    for index,row in enumerate(reader):
        #cliclo que recorre las columnas 
        for cont in range(15):
            #llenado de matriz con el archivo
            mat[index][cont] = row[cont]
    #Obetenemos las 14 propiedades de la nueva imagen
    imagen2P1 = primerCaracteristica(imgc,col,fil)
    imagen2P2=segundaCaracteristica(imgc, col,fil)               
    imagen2P3=tercerCaracteristica(imgc, col,fil)               
    imagen2P4=cuartaCaracteristica(imgc, col,fil)               
    imagen2P5=quintaCaracteristica(imgc, col,fil)               
    imagen2P6=sextaCaracteristica(imgc, col,fil)               
    imagen2P7=septimaCaracteristica(imgc, col,fil)               
    imagen2P8=octavaCaracteristica(imgc, col,fil)              
    imagen2P9=novenaCaracteristica(imgc, col,fil)               
    imagen2P10=decimaCaracteristica(imgc, col,fil)             
    imagen2P11=onceavaCaracteristica(imgc, col,fil)             
    imagen2P12=doceavaCaracteristica(imgc, col,fil)             
    imagen2P13=treceavaCaracteristica(imgc, col,fil)            
    imagen2P14=catorceavaCaracteristica(imgc, col,fil)             
    for val in range(2369):
        #obtenemos las 14 propiedades del dataSet
        p1 = float(mat[val+1][0])
        p2 = float(mat[val+1][1])
        p3 = float(mat[val+1][2])
        p4 = float(mat[val+1][3])
        p5 = float(mat[val+1][4])
        p6 = float(mat[val+1][5])
        p7 = float(mat[val+1][6])
        p8 = float(mat[val+1][7])
        p9 = float(mat[val+1][8])        
        p10 = float(mat[val+1][9])
        p11 = float(mat[val+1][10])
        p12 = float(mat[val+1][11])
        p13 = float(mat[val+1][12])
        p14 = float(mat[val+1][13])
        #aplicamos la formula euclidiana
        dist = math.sqrt(((p1-imagen2P1)**2)+((p2-imagen2P2)**2)+((p3-imagen2P3)**2)+((p4-imagen2P4)**2)+((p5-imagen2P5)**2)+((p6-imagen2P6)**2)+((p7-imagen2P7)**2)+((p8-imagen2P8)**2)+((p9-imagen2P9)**2)+((p10-imagen2P10)**2)+((p11-imagen2P11)**2)+((p12-imagen2P12)**2)+((p13-imagen2P13)**2)+((p14-imagen2P14)**2))
        #almacenamos la distancia de la formula y lo almacenamos en la matriz knn        
        knn[val][0] = val+1
        knn[val][1] = dist
        #almacena la clase a la que pertenece
        knn[val][2] = mat[val+1][14]
    #matriz para datos del knn
    res=[]
    #ciclo que crea la matriz con ceros
    for x in range(numVeci):
        #llenado de matriz con ceros decimales
        res.append([0.0]*3)
    #obtenemos el numero de elementos de knn la cual contiene la distancia y
    #la posicion en el dataSet
    elementos = knn
    #apuntador para alamacenar distancia, posicion dataSet y la clase 
    apun = 0
    for i in range(numVeci):
        temp = elementos[0][1]
        numero = len(elementos)
        for j in range(numero):
            if(elementos[j][1] < temp):
                temp = elementos[j][1]
                apun = j 
            if (j+1==numero):
                res[i][0] = elementos[apun][0]
                res[i][1] = elementos[apun][1]
                res[i][2] = elementos[apun][2]
                elementos.pop(apun)
    #regresamos el conjunto de elementos que son distancia, posicion y clase
    return res

#----------------------------------------------------------------------------
#Parte del código que se va a ejecutar primero
#----------------------------------------------------------------------------
nomImg = input('¿Qué imagen deseas buscar? ')
numVeci = int(input('Ingresa el número de vecinos: '))
nomImg = nomImg+".png"
mat = kNN(nomImg, numVeci)
#----------------------------------------------------------------------------
#Información general del DataSet
#----------------------------------------------------------------------------
print("________________________________________________________________________")
print("              Información general del Dataset cargado")
print("________________________________________________________________________")
print("Numero de instancias en el dataSet: 2369")
print("Numero de Caracteristicas: 14")
print("Numero de clases: 10")
print("Clases: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
print("________________________________________________________________________")
print("                               KNN")
#----------------------------------------------------------------------------
#Información general de KNN
#----------------------------------------------------------------------------
print("Vecino: \t"+"Posición dataSet: \t"+"Clase: \t"+"Distancia:\t")
print("________________________________________________________________________")
for va in range(numVeci):
    print("   "+str(va+1)+"\t"+"        "+str(mat[va][0])+" \t  "+str(mat[va][2])+"\t"+"%.10f"%mat[va][1])
    #Utilizamos if para contabilizar el numero de vecinos que encuentre la nueva imagen
    if(mat[va][2]=='0'):
        contadorCero = contadorCero+1
    elif(mat[va][2]=='1'):
        contadorUno = contadorUno+1
    elif(mat[va][2]=='2'):
        contadorDos = contadorDos+1
    elif(mat[va][2]=='3'):
        contadorTres = contadorTres+1
    elif(mat[va][2]=='4'):
        contadorCuatro = contadorCuatro+1
    elif(mat[va][2]=='5'):
        contadorCinco = contadorCinco+1
    elif(mat[va][2]=='6'):
        contadorSeis = contadorSeis+1
    elif(mat[va][2]=='7'):
        contadorSiete = contadorSiete+1
    elif(mat[va][2]=='8'):
        contadorOcho = contadorOcho+1 
    elif(mat[va][2]=='9'):
        contadorNueve = contadorNueve+1        
print("________________________________________________________________________")
print("               Informe final sobre vecinos de KNN ")
#----------------------------------------------------------------------------
#Información general detallada de la salida del programa
#----------------------------------------------------------------------------
print("Instancias "+"Clase "+"Vecinos encontrados")
print("________________________________________________________________________")
print("   237"+"   "+"    0"+"          "+str(contadorCero))
print("   237"+"   "+"    0"+"          "+str(contadorUno))
print("   237"+"   "+"    0"+"          "+str(contadorDos))
print("   237"+"   "+"    0"+"          "+str(contadorTres))
print("   237"+"   "+"    0"+"          "+str(contadorCuatro))
print("   237"+"   "+"    0"+"          "+str(contadorCinco))
print("   237"+"   "+"    0"+"          "+str(contadorSeis))
print("   237"+"   "+"    0"+"          "+str(contadorSiete))
print("   237"+"   "+"    0"+"          "+str(contadorOcho))
print("   237"+"   "+"    0"+"          "+str(contadorNueve))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('              La Imagen pertenece a la clase ',mat[0][2])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")