# Evidencia 1
# Carolina Lara Suaáez A0368710

# Encontrar los índices de aparición de cada uno de los tres genes (gen M, S y ORF1AB) en la secuencia del virus SARS-COV-2-MN908947.3.txt.
# Por cada gen muestra su nombre, índices de aparición en la secuencia del virus y primeros 12 caracteres.

# Implementación del algoritmo KMP para buscar patrones en un texto

def cargar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    # Omitir la primera línea (índice 0) y unir el resto en una sola cadena.
    contenido = ''.join(lineas[1:])
    return  contenido

# Nombre de los archivos para cada gen.
archivo_gen_M = 'gen-M.txt'
archivo_gen_S = 'gen-S.txt'
archivo_gen_ORF1AB = 'gen-ORF1AB.txt'
archivo_SARS_COV2_MN = 'SARS-COV-2-MN908947.3.txt'
archivo_SARS_COV2_MT = 'SARS-COV-2-MT007544.1.txt'

# Carga cada archivo en una variable.
gen_M = cargar_archivo(archivo_gen_M)
gen_S = cargar_archivo(archivo_gen_S)
gen_ORF1AB = cargar_archivo(archivo_gen_ORF1AB)
secuencia_virus = cargar_archivo(archivo_SARS_COV2_MN)




def buscar_gen_en_secuencia(gen_nombre, gen_patron, secuencia):
    print(f"\nBuscando gen {gen_nombre} en la secuencia...")
    indices = []
    inicio = 0
    while True:
        inicio = secuencia.find(gen_patron, inicio)
        if inicio == -1:
            break
        fin = inicio + len(gen_patron)
        ocurrencia = secuencia[inicio:fin]
        indices.append((inicio, ocurrencia[:12]))
        inicio = fin
    return indices

# Buscar y mostrar el gen M en la secuencia del virus
indices_gen_M = buscar_gen_en_secuencia("M", gen_M,secuencia_virus )
print(f"\nÍndices de aparición del gen M en la secuencia del virus SARS-COV-2-MN908947.3.txt:")
for indice, primeros_12 in indices_gen_M:
    print(f"Nombre: M, Índice: {indice}, Primeros 12 caracteres: {primeros_12}")

# Buscar y mostrar el gen S en la secuencia del virus
indices_gen_S = buscar_gen_en_secuencia("S", gen_S, secuencia_virus)
print(f"\nÍndices de aparición del gen S en la secuencia del virus SARS-COV-2-MN908947.3.txt:")
for indice, primeros_12 in indices_gen_S:
    print(f"Nombre: S, Índice: {indice}, Primeros 12 caracteres: {primeros_12}")

# Buscar y mostrar el gen ORF1AB en la secuencia del virus
indices_gen_ORF1AB = buscar_gen_en_secuencia("ORF1AB", gen_ORF1AB, secuencia_virus)
print(f"\nÍndices de aparición del gen ORF1AB en la secuencia del virus SARS-COV-2-MN908947.3.txt:")
for indice, primeros_12 in indices_gen_ORF1AB:
    print(f"Nombre: ORF1AB, Índice: {indice}, Primeros 12 caracteres: {primeros_12}")


print("Contenido del gen M:")
print(gen_M[:200])  # Imprime los primeros 200 caracteres del gen M como ejemplo
print("\nContenido del gen S:")
print(gen_S[:200])  # Imprime los primeros 200 caracteres del gen S como ejemplo
print("\nContenido del gen ORF1AB:")
print(gen_ORF1AB[:200])  # Imprime los primeros 200 caracteres del gen ORF1AB como ejemplo