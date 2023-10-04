aminoacido_dict = {
    "A": ["GCT", "GCC", "GCA", "GCG"],
    "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "N": ["AAT", "AAC"],
    "D": ["GAT", "GAC"],
    "B": ["AAT", "AAC", "GAT", "GAC"],
    "C": ["TGT", "TGC"],
    "Q": ["CAA", "CAG"],
    "E": ["GAA", "GAG"],
    "Z": ["CAA", "CAG", "GAA", "GAG"],
    "G": ["GGT", "GGC", "GGA", "GGG"],
    "H": ["CAT", "CAC"],
    "I": ["AAT", "ATC", "ATA"],
    "L": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
    "K": ["AAA", "AAG"],
    "M": ["ATG"],
    "F": ["TTT", "TTC"],
    "P": ["CCT", "CCC", "CCA", "CCG"],
    "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "T": ["ACT", "ACC", "ACA", "ACG"],
    "W": ["TGG"],
    "Y": ["TAT", "TAC"],
    "V": ["GTT", "GTC", "GTA", "GTC"]
}


# La cadena de aminoácidos que deseas traducir
cadena_aminoacidos = "MGYINVFAFPFTIYSLLLCRMNSRNYIAQVDVVNFNLT"

def traducit_a_codones(cadena_aminoacidos):
    cadena_codones = "ATG"
    for index in range(0, 6):
        for aminoacido in cadena_aminoacidos:
            # Si el aminoacido esta en el diccionario de aminoacidos
            if aminoacido in aminoacido_dict:
                # Acceder al primer codon del aminoacido
                cadena_codones += aminoacido_dict[aminoacido][0]
            
    # Regresar la cadena de codones como una cadena de texto
    return cadena_codones

 
# 4.Compara las versiones del genoma del virus de Wuhan, 2019 vs Texas, 2020. Determina donde  difieren, y si tales diferencias resultan en aminoácidos diferentes.
# Lista los índices donde encuentres diferencias, muestra los codones afectados por tal diferencia y el aminoácido producido por cada versión.

def load_file(file_name): # Cargar el archivo y devolver su contenido
    with open(file_name, 'r') as file:
        next(file)
        return file.read().replace('\n', '') # Omitir la primera línea


def longest_common_substring(s1, s2): # Encontrar la subcadena común más larga entre dos cadenas
    n = len(s1) # Longitud de la primera cadena
    m = len(s2) # Longitud de la segunda cadena
    max_len = 0
    end_index = 0


    dp = [[0] * (m + 1) for _ in range(n + 1)] # Matriz para almacenar la longitud de la subcadena común más larga

    for i in range(1, n + 1):  # Iterar sobre cada posición de la primera cadena
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1 # Si los caracteres son iguales, agregar 1 a la longitud de la subcadena común más larga
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i # Actualizar la longitud máxima y el índice final de la subcadena común más larga


    common_substring = s1[end_index - max_len:end_index] # Extraer la subcadena común más larga

    return common_substring


def translate_to_amino_acids(dna_sequence): # Traducir una secuencia de ADN a una secuencia de aminoácidos

    codon_to_aa = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
        "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    }


    amino_acids = "" # Cadena para almacenar los aminoácidos
    codon = "" # Cadena para almacenar los codones


    for base in dna_sequence: # Iterar sobre cada base de la secuencia de ADN
        codon += base # Agregar la base al codón
        if len(codon) == 3: # Si el codón está completo
            amino_acid = codon_to_aa.get(codon, 'X') # Obtener el aminoácido
            amino_acids += amino_acid # Agregar el aminoácido a la cadena
            codon = ""

    return amino_acids # Devolver la cadena de aminoácidos


sequence_wuhan = load_file('SARS-COV-2-MN908947.3.txt') # Cargar la secuencia de Wuhan
sequence_texas = load_file('SARS-COV-2-MT106054.1.txt') # Cargar la secuencia de Texas

common_substring = longest_common_substring(sequence_wuhan, sequence_texas) # Encontrar la subcadena común más larga

differences = [(i, wuhan, texas) for i, (wuhan, texas) in enumerate(zip(sequence_wuhan, sequence_texas)) if wuhan != texas] # Encontrar las diferencias entre las secuencias

for i, wuhan, texas in differences: # Iterar sobre cada diferencia
    print(f"Posición  {i + 1}: Wuhan: {wuhan}, Texas: {texas}") # Imprimir la posición y los nucleótidos involucrados
    codon_start = max(i - 2, 0) # Obtener el índice de inicio del codón
    codon_end = min(i + 3, len(sequence_wuhan)) # Obtener el índice final del codón
    affected_codon = sequence_wuhan[codon_start:codon_end] # Obtener el codón afectado
    amino_acid_wuhan = translate_to_amino_acids(affected_codon) # Traducir el codón afectado a aminoácidos
    amino_acid_texas = translate_to_amino_acids(affected_codon.replace(wuhan, texas)) # Traducir el codón afectado a aminoácidos
    print(f"Codon Afectado : {affected_codon}") # Imprimir el codón afectado
    print(f"Aminoacido (Wuhan): {amino_acid_wuhan}") # Imprimir el aminoácido producido por el codón afectado en Wuhan
    print(f"Aminoacido (Texas): {amino_acid_texas}") # Imprimir el aminoácido producido por el codón afectado en Texas
    print("---")

