def cargar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        archivo.readline()  # Omitir la primera línea
        contenido = archivo.read().replace('\n', '')
    return contenido

def manacher_algorithm(S):
    t = '#' + '#'.join(S) + '#'  # Agregar caracteres especiales
    n = len(t)
    p = [0] * n  # Lista para almacenar la longitud de palíndromos centrados en cada posición.

    c = r = 0  # Posición central y su correspondiente límite derecho.

    for i in range(1, n - 1):
        i_mirror = 2 * c - i  # Espejo de la posición i con respecto al centro c.

        if r > i:
            # Si i está dentro del límite derecho r, aprovechamos información previa.
            p[i] = min(r - i, p[i_mirror])

        # Expandir el palíndromo centrado en i.
        while (i + 1 + p[i] < n) and (i - 1 - p[i] >= 0) and (t[i + 1 + p[i]] == t[i - 1 - p[i]]):
            p[i] += 1

        # Si el palíndromo centrado en i se extiende más allá del límite derecho r, actualizar c y r.
        if i + p[i] > r:
            c, r = i, i + p[i]

    # Encontrar el palíndromo más largo y su posición.
    max_len, center_index = max((n, i) for i, n in enumerate(p))
    start = (center_index - max_len) // 2
    end = start + max_len - 1

    return S[start:end + 1]

# Nombres de los archivos
archivo_gen_M = 'gen-M.txt'
archivo_gen_ORF1AB = 'gen-ORF1AB.txt'
archivo_gen_S = 'gen-S.txt'

# Cargar el contenido de los archivos
contenido_gen_M = cargar_archivo(archivo_gen_M)
contenido_gen_ORF1AB = cargar_archivo(archivo_gen_ORF1AB)
contenido_gen_S = cargar_archivo(archivo_gen_S)

# Encontrar los palíndromos más largos en cada archivo
palindromo_gen_M = manacher_algorithm(contenido_gen_M)
palindromo_gen_ORF1AB = manacher_algorithm(contenido_gen_ORF1AB)
palindromo_gen_S = manacher_algorithm(contenido_gen_S)

# Guardar los resultados en archivos
with open("palindromos.txt", "w") as archivo:
    archivo.write("gen-M: " + palindromo_gen_M + "\n")
    archivo.write("gen-ORF1AB: " + palindromo_gen_ORF1AB + "\n")
    archivo.write("gen-S: " + palindromo_gen_S + "\n")

# Imprimir los resultados
print("gen-M: " + palindromo_gen_M)
print("gen-ORF1AB: " + palindromo_gen_ORF1AB)
print("gen-S: " + palindromo_gen_S)

