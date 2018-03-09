import math

colColores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
colElementosXColor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#funcion que retorna un vector, donde se almacenas todas las lineas leidas en el fichero con ruta rutaFichero
def obtenerListaLineas(rutaFichero):
    lista = []
    archivo = open(rutaFichero, "r")
    for linea in archivo.readlines():
        lineaFiltrada = linea.strip("\n")
        lineaFiltrada = linea.replace(",", ".")
        lista.append(lineaFiltrada)
    archivo.close()
    return lista

def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)

#funcion encargada de crear una matriz con una dimension recibida como parametro y la llena con los elementos de la coleccion listaElementos tambien que recibe como parametro
def crearMatriz(listaElementos, dimension):
    matriz = []
    for fila in range(0, len(listaElementos), dimension):
        sublista = listaElementos[fila: fila + dimension] #extrae la lista por intervalos
        matriz.append(sublista)
    return matriz

#funcion encargada de retornar una coleccion de tuplas, cada tupla contiene el indice de la fila junto con el indice de la columna de los valores que duperaron el umbral recibido como parametro
def obtenerColTuplasIndicesElementosFiltrados(matrizElementos, umbral):
     coleccionTuplas = []
     for indiceFila in range(0, len(matrizElementos)):
         fila = matrizElementos[indiceFila]
         for indiceColumna in range(0, len(fila)):
             numero = float(fila[indiceColumna])
             if (numero > umbral):
                 coleccionTuplas.append((indiceFila, indiceColumna))                
     return coleccionTuplas

def obtenerTuplasConfictoEnMapeoColorAMatriz(colTuplasIndices, matrizGrupos, color):
    global colElementosXColor    
    colTuplasConflicto = []
    indiceColor = colColores.index(color)
    for coordenada in colTuplasIndices:
        fila, columna = coordenada[0], coordenada[1]        
        colorEnCoordenada = matrizGrupos[fila][columna]
        if (colorEnCoordenada == 0):
            matrizGrupos[fila][columna] = color
        else:
            matrizGrupos[fila][columna] = (colorEnCoordenada, color)
            colTuplasConflicto.append((fila, columna))
        colElementosXColor[indiceColor] = colElementosXColor[indiceColor] + 1  
    return colTuplasConflicto      

def resolverConflictos(colTuplasConflicto, matrizGrupos):
    global colElementosXColor
    for tupla in colTuplasConflicto:
        fila, columna = tupla[0], tupla[1]
        tuplaColores = matrizGrupos[fila][columna]
        colorAnterior, colorNuevo = tuplaColores[0], tuplaColores[1]
        indiceColorAnterior, indiceColorNuevo = colColores.index(colorAnterior), colColores.index(colorNuevo)
        if colElementosXColor[indiceColorAnterior] >= colElementosXColor[indiceColorNuevo]:
            colElementosXColor[indiceColorNuevo] = colElementosXColor[indiceColorNuevo] - 1
            matrizGrupos[fila][columna] = colorAnterior
        else:
            colElementosXColor[indiceColorAnterior] = colElementosXColor[indiceColorAnterior] - 1
            matrizGrupos[fila][columna] = colorNuevo

def procesarLinea(matrizGrupos, colElementos, umbral, color):
    dimension = len(matrizGrupos)
    matrizDeLinea = crearMatriz(colElementos, dimension)

    print("\nMOSTRANDO: matriz de linea ----------------------------------")

    imprimirMatriz(matrizDeLinea)

    coleccionTuplasMapear = obtenerColTuplasIndicesElementosFiltrados(matrizDeLinea, umbral)
    tuplasConflicto = obtenerTuplasConfictoEnMapeoColorAMatriz(coleccionTuplasMapear, matrizGrupos, color)

    print("\nMOSTRANDO: Matriz de grupos ----------------------------------")

    imprimirMatriz(matrizGrupos)

    print("\nMOSTRANDO: coleccion de elementos por color ----------------------------------")
    print(colElementosXColor)

    resolverConflictos(tuplasConflicto, matrizGrupos)

    print("\nMOSTRANDO: elementos por color ----------------------------------")
    print(colElementosXColor)




def main():    
    dimensionMatriz = 5
    listaLineas = obtenerListaLineas("salida.txt")
    #la siguiente linea de codigo hace que se genere un cero (range(1)) y se cree una fila A de un numero de ceros del tamanio de dimensionMatriz que esta antes del for, luego se crean replicas de la fila A, el numero de replicas es dimensionMatriz que esta despues del for
    matriz = [dimensionMatriz * range(1) for fila in range(dimensionMatriz)]

    for indiceLinea in range(0, len(listaLineas)):
        linea = listaLineas[indiceLinea]
        indiceColor = colElementosXColor.index(0)
        colElementos = linea.split(";")
        if (dimensionMatriz == math.sqrt(len(colElementos))):
            procesarLinea(matriz, colElementos, 0.85, colColores[indiceColor])        
        else:
            print("Error: dimension de matriz distinta a numero de elementos por linea")
            break
    print("\nMatriz Resultado: -------------------------------------\n")
    imprimirMatriz(matriz)

main()    






