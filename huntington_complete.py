sequence = "" # Variable vacía para almacenar la secuencia de ADN.

# Función para contar la máxima cantidad de repeticiones consecutivas de CAG.
def CAG_count(sequence):
    codon_counter = 0     # Contador de repeticiones consecutivas de CAG.
    max_counter = 0       # Almacena el máximo de repeticiones consecutivas de CAG.

    # Itera sobre la secuencia en pasos de 3 nucleótidos (un codón).
    for nuc in range(0, len(sequence), 3):
        codon = sequence[nuc:nuc + 3]  # Extrae un codón de 3 nucleótidos.

        # Comprueba si el codón es "CAG".
        if codon == "CAG":
            codon_counter += 1  # Incrementa el contador si es CAG.
        else:
            # Si termina las repticiones de CAG, compara y actualiza el máximo.
            if codon_counter > max_counter:
                max_counter = codon_counter
            codon_counter = 0  # Reinicia el contador para la siguiente serie de CAG si hay.

    # Devuelve el máximo de CAG encontradas.
    return max_counter


# Función que clasifica el riesgo según la cantidad de CAG.
def risk(max_counter):
    # Revisa la cantidad de repeticiones y clasifica el riesgo.
    if CAG_count(sequence) < 27:
        return "rango normal, no hay riesgo"
    elif CAG_count(sequence) >= 27 and CAG_count(sequence) < 36:
        return "riesgo bajo"
    elif CAG_count(sequence) >= 36 and CAG_count(sequence) < 40:
        return "riesgo moderado, posibilidad de síntomas"
    elif CAG_count(sequence) >= 40 and CAG_count(sequence) < 56:
        return "riesgo alto"
    elif CAG_count(sequence) >= 56:
        return "riesgo alto, alta posibilidad de inicio temprano"
    else:
        return "término inválido"  # Por si falla.


# Abre el archivo de con la secuencia
with open("huntington_sequence.txt") as file:
    for line in file:
        # Salta lineas comienzan con ">", típicas de encabezados en archivos FASTA, y lee las que no.
        if not line.startswith(">"):
            line = line.rstrip("\n")  # Elimina saltos de línea al final.
            sequence += line  # Añade la línea a la variable sequence.
            sequence = sequence.upper()  # Convierte a mayúscula, por si hay algún error.

# Imprime el máximo de repeticiones de CAG.
print(f"La secuencia CAG se repite {CAG_count(sequence)} veces")

# Evalúa el riesgo.
print(f"Según lo anterior, se clasifica como {risk(CAG_count(sequence))}")
