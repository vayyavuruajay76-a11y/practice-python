def to_rna(dna_strand):
    rna_strand=''
    for x in dna_strand:
        if x=='A':
            rna_strand+='U'
        elif x=='T':
            rna_strand+='A'
        elif x=='G':
            rna_strand+='C'
        elif x=='C':
            rna_strand+='G'
        else:
            rna_strand+=x

    return rna_strand
