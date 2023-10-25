#Jense David Martinez Tobón - 1004685332
#Isaac Pachón Zuleta - 1004529703

#Se importan las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np

def main():
    #Cargamos la imagen termica
    imagen_tiff = np.array(plt.imread("C:./img/FLIR_00641.tiff"))   
    D = np.double(imagen_tiff)
    tem_min=-40
    tem_max=160
    NBits=14
    matriz_centi = np.array((tem_max-tem_min)*D/2**NBits+tem_min)

    #Calculamos y obtenemos los datos requeridos en el taller
    promedio = promedio_matriz(matriz_centi)
    mediana = mediana_matriz(matriz_centi)
    moda = moda_matriz(matriz_centi)
    maxima, coordenadas_maxima = maxima_matriz(matriz_centi)
    minima, coordenadas_minima = minima_matriz(matriz_centi)

    #Creamos la figura de la imagen termica
    fig = plt.figure("Imagen Termografica")
    plt.plot(coordenadas_maxima[0],coordenadas_maxima[1], marker="D", color="magenta")
    plt.plot(coordenadas_minima[0],coordenadas_minima[1], marker="D", color="cyan")
    plt.imshow(matriz_centi,cmap = plt.cm.hot_r)
    plt.colorbar(shrink=.92)
    
    #Creamos la figura del histograma
    plt.figure("Histograma")
    hist,bins = np.histogram(matriz_centi,np.arange(0,tem_max),density=True)
    HistoTempeBar = np.int32(matriz_centi.round())
    plt.hist(HistoTempeBar,5,facecolor="red",alpha = 0.5)
    minima_matriz(matriz_centi)

    #Imprimimos en pantalla los datos obtenidos
    print("Promedio: ",round(promedio,2))
    print("Mediana: ",round(mediana,2))
    print("Moda: ",round(moda,2))
    print("Temperatura maxima ",round(maxima,2)," en el punto ", coordenadas_maxima)
    print("Temperatura minima ",round(minima,2)," en el punto ", coordenadas_minima)
    
    plt.show()

# Esta  funcion se encarga de sumar todos los elementos de una matriz
def suma_matriz(matriz):
    filas, col = np.shape(matriz)
    suma = 0
    for i in range(filas):
        for j in range(col):
            suma += matriz[i,j]
    return suma

#Esta funcion se encarga de calcular cuantos elementos tiene una matriz
def num_elementos_matriz(matriz):
    filas, col = np.shape(matriz)
    s = 0
    for i in range(filas):
        for j in range(col):
            s += 1
    return s

#Esta funcion se encargar de calcular el promedio de los datos de la matriz
def promedio_matriz(matriz):
    suma = suma_matriz(matriz)
    elementos = num_elementos_matriz(matriz)
    return suma/elementos

#Esta funcion se encarga de obtener el dato maximo dentro de una matriz
def maxima_matriz(matriz):
    filas, col = np.shape(matriz)
    coordenadas = (0,0)
    n_mayor = matriz[0,0]
    for i in range(filas):
        for j in range(col):
            if  matriz[i,j] > n_mayor:
                n_mayor = matriz[i,j]
                coordenadas = (j,i)
    return n_mayor, coordenadas

#Esta funcion se encarga de obtener el dato minimo dentro de una matriz
def minima_matriz(matriz):
    filas, col = np.shape(matriz)
    n_menor = matriz[0,0]
    coordenadas = (0,0)
    for i in range(filas):
        for j in range(col):
            if  matriz[i,j] < n_menor:
                n_menor = matriz[i,j]
                coordenadas = (j,i)
    return n_menor, coordenadas

#Esta funcion se encarga de calcular la mediana de una matriz
def mediana_matriz(matriz):
    filas, col = np.shape(matriz)
    numero_elementos = num_elementos_matriz(matriz)
    lista_ord = []
    if ((numero_elementos % 2) == 0):
        pos_mediana = round((((numero_elementos/2) + ((numero_elementos/2) + 1)) / 2))
    else:
        pos_mediana = (numero_elementos + 1) / 2

    for i in range(filas):
        for j in range(col):
            lista_ord.append(matriz[i,j])

    lista_ord.sort()
    for i in range(0,len(lista_ord)-1):
        if (i == (pos_mediana-1)):
            mediana = lista_ord[i]

    return mediana

#Esta funcion se encarga de calcular la moda de una matriz    
def moda_matriz(matriz):
    filas, col = np.shape(matriz)
    lista = []
    repeticiones = {}
    moda = None
    repeticion_max = 0

    for i in range(filas):
        for j in range(col):
            lista.append(matriz[i,j])

    for elemento in lista:
        repeticiones[elemento] = repeticiones.get(elemento,0) + 1

    for elemento, repeticion in repeticiones.items():
        if (repeticion > repeticion_max):
            moda = elemento
            repeticion_max = repeticion

    return moda

main()

