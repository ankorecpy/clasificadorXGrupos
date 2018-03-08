colColores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
colElementosXColor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#funcion que retorna un vector, donde se almacenas todas las lineas leidas en el fichero con ruta rutaFichero
def obtenerListaLineas(rutaFichero):
    lista = []
    archivo = open(rutaFichero, "r")
    for linea in archivo.readlines():
        lista.append(linea)
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

def procesarLinea(matrizGrupos, linea, umbral, separador, color):
    dimension = len(matrizGrupos)
    listaElementos = linea.split(separador)
    if ((len(listaElementos) % dimension) == 0):

        matrizDeLinea = crearMatriz(listaElementos, dimension)
        print("\nMOSTRANDO: matriz de linea ----------------------------------")
        imprimirMatriz(matrizDeLinea)

        coleccionTuplasMapear = obtenerColTuplasIndicesElementosFiltrados(matrizDeLinea, umbral)
        tuplasConflicto = obtenerTuplasConfictoEnMapeoColorAMatriz(coleccionTuplasMapear, matrizGrupos, color)
        print("\nMOSTRANDO: Matriz de grupos ----------------------------------")
        imprimirMatriz(matrizGrupos)
        print("\nMOSTRANDO: coleccion de elementos por color ----------------------------------")
        print(colElementosXColor)
        print("\nMOSTRANDO: tuplas en conflicto ----------------------------------")
        print(tuplasConflicto)

    else:
        print ("Error: la cantidad de elementos de la linea es diferente al numero de columnas")



def main():    
    #dato 3 de prueba
    dimensionMatriz = 4
    indiceColor = 0
    listaLineas = obtenerListaLineas("testDatos.txt")
    #la siguiente linea de codigo hace que se genere un cero (range(1)) y se cree una fila A de un numero de ceros del tamanio de dimensionMatriz que esta antes del for, luego se crean replicas de la fila A, el numero de replicas es dimensionMatriz que esta despues del for
    matriz = [dimensionMatriz * range(1) for fila in range(dimensionMatriz)]

    for linea in range(2):
        procesarLinea(matriz, listaLineas[linea], 50, ";", colColores[indiceColor])
        indiceColor = indiceColor + 1

main()    



