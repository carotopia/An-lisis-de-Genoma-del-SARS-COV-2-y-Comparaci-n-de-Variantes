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

if __name__ == "__main__":
    print(traducit_a_codones(cadena_aminoacidos))