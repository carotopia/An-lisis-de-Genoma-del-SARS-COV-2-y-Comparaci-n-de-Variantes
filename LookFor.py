import re

# Patrón de búsqueda (sin el fragmento completo para evitar problemas de formato)
patron_busqueda = r'ATGGCAGATTCCAACGGTACTATTACCGTTGAAGAGCTTAAAAAGCTCCTTGAACAATGGAACCTAGTAATAGGTTTCCTATTCCTTACATGGATTTGTCTTCTACAATTTGCCTATGCCAACAGGAATAGGTTTTTGTA'

with open('SARS-COV-2-MN908947.3.txt', 'r') as file:
    contenido = file.read()
    if re.search(patron_busqueda, contenido):
        print("Se encontró el patrón en el archivo.")
    else:
        print("No se encontró el patrón en el archivo.")
