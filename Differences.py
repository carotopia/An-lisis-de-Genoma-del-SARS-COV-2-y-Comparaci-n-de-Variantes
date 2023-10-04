# Diccionario de traducción
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
    "IAQ": "Ile",
    "VDV": "Val",
    "VNF": "Val",
    "NLT": "Leu",
    "GGS": "Gly",
    "GCS": "Ala",
    "GCA": "Ala",
    "GCC": "Ala",
    "GGT": "Pro",
    "GGC": "Pro",
    "GGA": "Pro",
    "GGG": "Pro",
    "GAT": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "GTN": "Gln",
    "GTC": "Gln",
    "GTA": "Val",
    "GTG": "Val",
    "GYS": "Cys",
    "GYT": "Trp",
    "GYT": "Cys",
    "GYT": "Trp",
    "GGG": "Arg",
    "GGA": "Gly",
    "GGC": "Ala",
    "GGG": "Gly",
    "GGA": "Ala",
    "GGC": "Ala",
    "GTT": "Val",
    "GTC": "Val",
    "GTA": "Val",
    "GTG": "Val",
    "TTA": "Leu",
    "TTG": "Leu",
    "CTT": "Leu",
    "CTC": "Leu",
    "CTA": "Leu",
    "CTG": "Leu",
    "TAT": "Tyr",
    "TAC": "Tyr",
    "TAA": "Stop",
    "TAG": "Stop",
    "ATG": "Met",
    "ATC": "Ile",
    "ATA": "Ile",
    "ATT": "Ile",
    "ACA": "Thr",
    "ACC": "Thr",
    "ACT": "Thr",
    "ACG": "Thr",
    "AAT": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "AGT": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",
    "CCT": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "CAT": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",
    "CGT": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg"
}

aminoacido_dict = {
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Asn": ["AAT", "AAC"],
    "Asp": ["GAT", "GAC"],
    "Cys": ["TGT", "TGC"],
    "Gln": ["CAA", "CAG"],
    "Glu": ["GAA", "GAG"],
    "Gly": ["GGT", "GGC", "GGA", "GGG"],
    "His": ["CAT", "CAC"],
    "Ile": ["ATT", "ATC", "ATA"],
    "Leu": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
    "Lys": ["AAA", "AAG"],
    "Met": ["ATG"],
    "Phe": ["TTT", "TTC"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "Trp": ["TGG"],
    "Tyr": ["TAT", "TAC"],
    "Val": ["GTT", "GTC", "GTA", "GTG"],
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
