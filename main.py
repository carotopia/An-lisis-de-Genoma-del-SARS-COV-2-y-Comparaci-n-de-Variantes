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
    return contenido


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


def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_function[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_function[length - 1]
            else:
                prefix_function[i] = 0
                i += 1

    return prefix_function


def kmp_search(pattern, text):
    pattern = pattern.lower()
    text = text.lower()
    n = len(text)
    m = len(pattern)
    indices = []
    prefix_function = compute_prefix_function(pattern)
    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = prefix_function[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = prefix_function[j - 1]
            else:
                i += 1

    return indices


def buscar_gen_en_secuencia(gen_nombre, gen_patron, secuencia):
    print(f"\nBuscando gen {gen_nombre} en la secuencia...")
    indices = kmp_search(gen_patron, secuencia)
    return indices


# Buscar y mostrar el gen M en la secuencia del virus
indices_gen_M = buscar_gen_en_secuencia("M", gen_M, secuencia_virus)
#print(f"\nÍndices de aparición del gen M en la secuencia del virus SARS-COV-2-MN908947.3.txt:")
for indice in indices_gen_M:
    primeros_12 = secuencia_virus[indice:indice + 12]
    #print(f"Nombre: M, Índice: {indice}, Primeros 12 caracteres: {primeros_12}")

# Buscar y mostrar el gen S en la secuencia del virus
indices_gen_S = buscar_gen_en_secuencia("S", gen_S, secuencia_virus)
#print(f"\nÍndices de aparición del gen S en la secuencia del virus SARS-COV-2-MN908947.3.txt:")
for indice in indices_gen_S:
    primeros_12 = secuencia_virus[indice:indice + 12]
    #print(f"Nombre: S, Índice: {indice}, Primeros 12 caracteres: {primeros_12}")

# Buscar y mostrar el gen ORF1AB en la secuencia del virus
indices_gen_ORF1AB = buscar_gen_en_secuencia("ORF1AB", gen_ORF1AB, secuencia_virus)
#print(f"\nÍndices de aparición del gen ORF1AB en la secuencia del virus SARS-COV-2-MN908947.3.txt:")
for indice in indices_gen_ORF1AB:
    primeros_12 = secuencia_virus[indice:indice + 12]
    #print(f"Nombre: ORF1AB, Índice: {indice}, Primeros 12 caracteres: {primeros_12}")


def manacher_algorithm(s):
    # Transformar la cadena de entrada en una cadena de caracteres especiales para lidiar con palíndromos de longitud impar.
    # Por ejemplo, "abc" se convierte en "^#a#b#c#$".
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n  # Lista para almacenar la longitud de palíndromos centrados en cada posición.
    c = r = 0  # Posición central y su correspondiente límite derecho.

    for i in range(1, n - 1):
        i_mirror = 2 * c - i  # Espejo de la posición i con respecto al centro c.

        if r > i:
            # Si i está dentro del límite derecho r, aprovechamos información previa.
            p[i] = min(r - i, p[i_mirror])

        # Expandir el palíndromo centrado en i.
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        # Si el palíndromo centrado en i se extiende más allá del límite derecho r, actualizar c y r.
        if i + p[i] > r:
            c, r = i, i + p[i]

    # Encontrar el palíndromo más largo y su posición.
    max_len, center_index = max((n, i) for i, n in enumerate(p))
    start = (center_index - max_len) // 2
    end = start + max_len - 1

    return s[start:end + 1]


# Encontrar el palíndromo más largo en el gen M
longest_palindrome_M = manacher_algorithm(gen_M)
print(f"Palíndromo más largo en el gen M: {longest_palindrome_M}")
with open('longest_palindrome_M.txt', 'w') as f:
    f.write(longest_palindrome_M)

# Encontrar el palíndromo más largo en el gen S
longest_palindrome_S = manacher_algorithm(gen_S)
print(f"Palíndromo más largo en el gen S: {longest_palindrome_S}")
with open('longest_palindrome_S.txt', 'w') as f:
    f.write(longest_palindrome_S)

# Encontrar el palíndromo más largo en el gen ORF1AB
longest_palindrome_ORF1AB = manacher_algorithm(gen_ORF1AB)
print(f"Palíndromo más largo en el gen ORF1AB: {longest_palindrome_ORF1AB}")
with open('longest_palindrome_ORF1AB.txt', 'w') as f:
    f.write(longest_palindrome_ORF1AB)
