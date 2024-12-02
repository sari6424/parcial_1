# Función para contar repeticiones de CAG según el ATG.
def CAG_count_ATG(sequence):
    max_reps_CAG = 0  # Máximo de repeticiones CAG.

    # Recorre la secuencia en busca de cada 'ATG'.
    for start_pos in range(len(sequence) - 2):
        if sequence[start_pos:start_pos + 3] == "ATG":  # Va de 3 en 3.
            codon_counter = 0
            read_counter = 0

            # Itera desde cada ATG.
            for nuc in range(start_pos, len(sequence), 3): # Va de 3 en 3.
                codon = sequence[nuc:nuc + 3]  #Revisa codones.
                if codon == "CAG":
                    codon_counter += 1
                else:
                    # Actualiza el máximo CAG si es necesario.
                    if codon_counter > read_counter:
                        read_counter = codon_counter
                    codon_counter = 0

            # Actualiza el máximo de repeticiones según los ATG si es necesario.
            if read_counter > max_reps_CAG:
                max_reps_CAG = read_counter

    return max_reps_CAG


# Clasificación del riesgo según cantidad de repeticiones de CAG.
def risk(max_counter):
    if CAG_count_ATG(sequence) < 27:
        return "rango normal, no hay riesgo"
    elif CAG_count_ATG(sequence) >= 27 and CAG_count_ATG(sequence) < 36:
        return "riesgo bajo"
    elif CAG_count_ATG(sequence) >= 36 and CAG_count_ATG(sequence) < 40:
        return "riesgo moderado, posibilidad de síntomas"
    elif CAG_count_ATG(sequence) >= 40 and CAG_count_ATG(sequence) < 56:
        return "riesgo alto"
    elif CAG_count_ATG(sequence) >= 56:
        return "riesgo alto, alta posibilidad de inicio temprano"
    else:
        return "término inválido"  # Por si falla o sucede algo extraño.

# Diccionario para el multi FASTA
sequences = {}  # Inicia diccionario vacio
seq_name = ""  # Para nos nombres de la secuencia al imprimir.

# Leer el archivo multi FASTA.
with open("htt_multi_seq.fasta") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            seq_name = line[1:]  # Guarda nombre sin ">"
            sequences[seq_name] = ""  # Secuencia vacía en el diccionario
        else:
            sequences[seq_name] += line.upper()  # Agrega secuencia, mayúscula por si hay errores.

# Archivo aparte para los resultados
with open("resultados_htt.txt", "w") as output_file:

    for seq_name in sequences:  # Usa las llaves de diccionario
        sequence = sequences[seq_name]  # Accede a la secuencia mediante la llave

        # Escribir resultados en el archivo
        output_file.write(f"Secuencia: {seq_name}\n")
        output_file.write(f"  La secuencia CAG se repite {CAG_count_ATG(sequence)} veces\n")
        output_file.write(f"  Clasificación de riesgo: {risk(CAG_count_ATG(sequence))}\n\n")

    print("Terminado")
