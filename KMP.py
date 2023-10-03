# Evidencia 1
# Carolina Lara Suaáez A0368710

# 1. Encontrar los índices de aparición de cada uno de los tres genes (gen M, S y ORF1AB) en la secuencia del virus SARS-COV-2-MN908947.3.txt.
# Por cada gen muestra su nombre, índices de aparición en la secuencia del virus y primeros 12 caracteres.

# Implementación del algoritmo KMP para buscar patrones en un texto

def cargar_archivo(nombre_archivo):  # Cargar el archivo y devolver su contenido
    with open(nombre_archivo, 'r') as archivo:
        archivo.readline()  # Omitir la primera línea
        contenido = archivo.read().replace('\n', '')  # Eliminar los saltos de línea
    return contenido  # Devolver el contenido del archivo


# Algoritmo KMP para buscar patrones en un texto
# Complejidad: O(n + m)
# n = longitud del texto
# m = longitud del patrón
# Dependiendo de la longitud del patrón, el algoritmo es más ediciente
def BusquedaKMP(pat, txt):  # El algoritmo recibe un patrón y el texto donde se buscará
    M = len(pat)  # M es la longitud del patrón
    N = len(txt)  # N es la longitud del texto

    lps = [0] * M  # Crear una lista para almacenar los valores de LPS
    j = i = 0  # j es el índice para pat[] e i es el índice para txt[]
    array_indices = []  # Crear una lista para almacenar los índices donde se encuentra el patrón

    def calcularArrayLPS(pat, M, lps):  # Funcion para calcular el array LPS
        len = 0  # Longitud del prefijo más largo

        var = lps[0]  # lps[0] siempre es 0
        i = 1  # i es el índice para pat[]

        while i < M:  # Mientras el indice de pat sea menor que la longitud del patrón
            if pat[i] == pat[len]:  # Si el caracter en el indice i es igual al caracter en el indice len
                len += 1
                lps[i] = len  # El valor de lps en el indice i es igual a len
                i += 1
            else:  # Si los caracteres no son iguales
                if len != 0:
                    len = lps[len - 1]  # Actualizar len al valor de lps en el indice len - 1
                else:
                    lps[i] = 0
                    i += 1

    calcularArrayLPS(pat, M, lps)  # Llamamos a la funcion que clacula el array LPS con el patron, el texto y el lps

    while i < N:  # Mientras que el indice del texto sea menor a la longitud del texto
        if pat[j] == txt[i]:  # Si el caracter en el indice j del patron es igual al caracter en el indice i del texto
            i += 1
            j += 1

        if j == M:
            array_indices.append(i - j)  # Agregar el indice donde se encuentra el patron
            j = lps[j - 1]

        elif i < N and pat[j] != txt[
            i]:  # Si el caracter en el indice j del patron es diferente al caracter en el indice i del texto
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1  # Incrementar el indice del texto

    return array_indices  # Devolver la lista de indices donde se encuentra el patron


def imprimirApariciones(nombre_gen, array_apariciones, contenido_gen):
    cadena = f"{nombre_gen}: Indices de aprición en {array_apariciones}"
    print(cadena)
    print("Primeros 12 caracteres ", contenido_gen[:11] + '\n')

# Definir los nombres de los archivos
archivo_gen_M = 'gen-M.txt' # Nombre del archivo que contiene el gen M
archivo_gen_S = 'gen-S.txt' # Nombre del archivo que contiene el gen S
archivo_gen_ORF1AB = 'gen-ORF1AB.txt' # Nombre del archivo que contiene el gen ORF1AB
archivo_SARS_COV2_MN = 'SARS-COV-2-MN908947.3.txt' # Nombre del archivo que contiene el gen SARS-COV2-MN908947.3

# Cargar el contenido de los archivos
contenido_gen_M = cargar_archivo(archivo_gen_M)
contenido_gen_S = cargar_archivo(archivo_gen_S)
contenido_gen_ORF1AB = cargar_archivo(archivo_gen_ORF1AB)
contenido_SARS_COV2_MN = cargar_archivo(archivo_SARS_COV2_MN)

# Buscar los patrones en el texto
gen_M_array = BusquedaKMP(contenido_gen_M, contenido_SARS_COV2_MN)
gen_S_array = BusquedaKMP(contenido_gen_S, contenido_SARS_COV2_MN)
gen_ORF1AB_array = BusquedaKMP(contenido_gen_ORF1AB, contenido_SARS_COV2_MN)

# Imprimir los resultados
print("-------------------------------------------------")
imprimirApariciones("gen-M", gen_M_array, contenido_gen_M)
print("-------------------------------------------------")
imprimirApariciones("gen-S", gen_S_array, contenido_gen_S)
print("-------------------------------------------------")
imprimirApariciones("gen-ORF1AB", gen_ORF1AB_array, contenido_gen_ORF1AB)

# ---------------------------------------------

