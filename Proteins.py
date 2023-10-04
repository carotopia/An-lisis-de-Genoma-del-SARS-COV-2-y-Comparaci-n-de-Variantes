
codon_dict = {
        "MGY": "Met",
        "INV": "Ile",
        "FAA": "Phe",
        "FPT": "Phe",
        "IYS": "Tyr",
        "LLL": "Leu",
        "CRM": "Cys",
        "NS": "Asn",
        "RNY": "Arg",
        "IAQ": "Ile",
        "VDV": "Val",
        "VNF": "Val",
        "NLT": "Leu"
    }

aminoacido_dict = {
        "Ala": ["GCT", "GCC", "GCA", "GCG"],
        "A": ["GCT", "GCC", "GCA", "GCG"],
        "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "Asn": ["AAT", "AAC"],
        "N": ["AAT", "AAC"],
        "Asp": ["GAT", "GAC"],
        "D": ["GAT", "GAC"],
        "Cys": ["TGT", "TGC"],
        "C": ["TGT", "TGC"],
        "Gln": ["CAA", "CAG"],
        "Q": ["CAA", "CAG"],
        "Glu": ["GAA", "GAG"],
        "E": ["GAA", "GAG"],
        "Gin": ["CAA", "CAG"],
        "Z": ["CAA", "CAG"],
        "Gly": ["GGT", "GGC", "GGA", "GGG"],
        "G": ["GGT", "GGC", "GGA", "GGG"],
        "His": ["CAT", "CAC"],
        "H": ["CAT", "CAC"],
        "Ile": ["ATT", "ATC", "ATA"],
        "I": ["ATT", "ATC", "ATA"],
        "START": ["ATG"],
        "lle": ["ATT", "ATC", "ATA"],
        "Leu": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
        "L": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
        "Lys": ["AAA", "AAG"],
        "K": ["AAA", "AAG"],
        "Met": ["ATG"],
        "M": ["ATG"],
        "Phe": ["TTT", "TTC"],
        "F": ["TTT", "TTC"],
        "Pro": ["CCT", "CCC", "CCA", "CCG"],
        "P": ["CCT", "CCC", "CCA", "CCG"],
        "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
        "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
        "Thr": ["ACT", "ACC", "ACA", "ACG"],
        "T": ["ACT", "ACC", "ACA", "ACG"],
        "Trp": ["TGG"],
        "W": ["TGG"],
        "Tyr": ["TAT", "TAC"],
        "Y": ["TAT", "TAC"],
        "Val": ["GTT", "GTC", "GTA", "GTG"],
        "V": ["GTT", "GTC", "GTA", "GTG"],
        "STOP": ["TAA", "TAG", "TGA"],
    }


def traducir_proteina_a_nucleotidos(cadena_proteina):
    codones_proteina = []
    # Traducir la cadena de proteínas al diccionario de codones
    for i in range(0, len(cadena_proteina), 3):
        codon = cadena_proteina[i:i + 3]
        if codon in codon_dict:
            codones_proteina.append(codon_dict[codon])
        else:
            raise ValueError(f"El codón {codon} no se encuentra en el diccionario.")

        nucleotidos = []
        # Traducir los aminoácidos del diccionario de aminoácidos a codones
        for aminoacido in codones_proteina:
            if aminoacido in aminoacido_dict:
                nucleotidos.extend(aminoacido_dict[aminoacido])
            else:
                raise ValueError(f"El aminoácido {aminoacido} no se encuentra en el diccionario de aminoácidos.")

        return ''.join(nucleotidos)

    # Ejemplo de uso

cadena_proteina = "MGYINVFAFPFTIYSLLLCRMNSRNYIAQVDVVNFNLT"
print("Secuencia de proteína:")
cadena_nucleotidos = traducir_proteina_a_nucleotidos(cadena_proteina)
print("Secuencia de nucleótidos resultante:")
print(cadena_nucleotidos)
import string


codon_dict = {
    "MGY": "Met",
    "INV": "Ile",
    "FAF": "Phe",
    "PFT": "Phe",
    "IYS": "Tyr",
    "LLL": "Leu",
    "CRM": "Cys",
    "NSR": "Asn",
    "NYI": "Arg",
    "AQV": "Ile",
    "VDV": "Val",
    "VNF": "Val",
    "NLT": "Leu"
}
aminoacido_dict = {
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "A": ["GCT", "GCC", "GCA", "GCG"],
    "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Asn": ["AAT", "AAC"],
    "N": ["AAT", "AAC"],
    "Asp": ["GAT", "GAC"],
    "D": ["GAT", "GAC"],
    "Cys": ["TGT", "TGC"],
    "C": ["TGT", "TGC"],
    "Gln": ["CAA", "CAG"],
    "Q": ["CAA", "CAG"],
    "Glu": ["GAA", "GAG"],
    "E": ["GAA", "GAG"],
    "Gin": ["CAA", "CAG"],
    "Z": ["CAA", "CAG"],
    "Gly": ["GGT", "GGC", "GGA", "GGG"],
    "G": ["GGT", "GGC", "GGA", "GGG"],
    "His": ["CAT", "CAC"],
    "H": ["CAT", "CAC"],
    "Ile": ["ATT", "ATC", "ATA"],
    "I": ["ATT", "ATC", "ATA"],
    "START": ["ATG"],
    "lle": ["ATT", "ATC", "ATA"],
    "Leu": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
    "L": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
    "Lys": ["AAA", "AAG"],
    "K": ["AAA", "AAG"],
    "Met": ["ATG"],
    "M": ["ATG"],
    "Phe": ["TTT", "TTC"],
    "F": ["TTT", "TTC"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "P": ["CCT", "CCC", "CCA", "CCG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "T": ["ACT", "ACC", "ACA", "ACG"],
    "Trp": ["TGG"],
    "W": ["TGG"],
    "Tyr": ["TAT", "TAC"],
    "Y": ["TAT", "TAC"],
    "Val": ["GTT", "GTC", "GTA", "GTG"],
    "V": ["GTT", "GTC", "GTA", "GTG"],
    "STOP": ["TAA", "TAG", "TGA"],
}

# La cadena de aminoácidos que deseas traducir
cadena_aminoacidos = "MGYINVFAFPFTIYSLLLCRMNSRNYIAQVDVVNFNLT"

# Función para traducir la cadena de aminoácidos a ARNm
def traducir_a_ARNm(cadena_aminoacidos):
    secuencia_arnm = ""
    for i in range(0, len(cadena_aminoacidos), 3):
        grupo = cadena_aminoacidos[i:i+3]
        aminoacido = codon_dict.get(grupo, 'XXX')  # Obtener el aminoácido
        if aminoacido != 'XXX':
            codones = aminoacido_dict.get(aminoacido, [])
            secuencia_arnm += "/".join(codones) + " "  # Agregar los codones del aminoácido
        else:
            secuencia_arnm += "XXX "  # Si no se encuentra el aminoácido, se agrega XXX
    return secuencia_arnm.strip()

# Llama a la función y muestra la secuencia de ARNm resultante
secuencia_arnm = traducir_a_ARNm(cadena_aminoacidos)
print(secuencia_arnm)
