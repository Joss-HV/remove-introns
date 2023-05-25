RNA_codon_tabla = {
# Segunda Base
# U C A G
# U
'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', # UxU
'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C', # UxC
'UUA': 'L', 'UCA': 'S', 'UAA': 'Stp', 'UGA': 'Stp', # UxA
'UUG': 'L', 'UCG': 'S', 'UAG': 'Stp', 'UGG': 'W', # UxG
# C
'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', # CxU
'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', # CxC
'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', # CxA
'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R', # CxG
# A
'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', # AxU
'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', # AxC
'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', # AxA
'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', # AxG
# G
'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', # GxU
'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', # GxC
'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', # GxA
'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G' # GxG
}

with open("H1F4.txt", "r") as fasta:
    linea = fasta.readlines()
    cadena = ''.join(linea[1:])
    cadena = cadena.replace("\n", "")
    cadena=cadena.replace("T", "U")

intron1=cadena[0:728]
cadena=cadena.replace(intron1, "")

codon_inicio = cadena.find("AUG")
i=codon_inicio
codon_stop = ["UAA","UAG","UGA"]
codon = cadena[i:i+3]
aminoacido = RNA_codon_tabla[codon]
cadena_traducida= ""

while codon not in codon_stop:
    codon = cadena[i:i + 3]
    aminoacido = RNA_codon_tabla[codon]
    cadena_traducida += aminoacido
    i += 3

print(linea[0])
print(cadena_traducida)


