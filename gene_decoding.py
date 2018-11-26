dna_strand_1 = "ATC-CGG-GAC-CAG-CTG-GCC-GTC" #TAG-GCC-CTG-GTC-GAC-CGG-CAG
dna_strand_2 = " "
for x in range (len(dna_strand_1)):
    char = dna_strand_1 [x]
    print (char,end =',')

    if char == "A":
        dna_strand_2 += "T"
    elif char == "T":
        dna_strand_2  += "A"
    elif char == "C":
        dna_strand_2  +="G"
    elif char == "G":
        dna_strand_2  += "C" \
                         ""
    else:
        dna_strand_2 +=char

print (dna_strand_2)
