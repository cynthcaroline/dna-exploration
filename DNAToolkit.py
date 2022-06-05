Nucleotides = ["A", "C", "G", "T"]

#check sequence to make sure it's dna string
#evaluate dna string
def validateSeq(dna_seq):
  tmpseq = dna_seq.upper() #temporary sequence
  for nuc in tmpseq:
    if nuc not in Nucleotides: #
      return False #false if not include in nucleotides

    return tmpseq

def countNucFrequency(seq): 
    tmpFreqDict = {"A": 0, "C":0, "G":0, "T":0} #dictionary
    for nuc in seq:
        tmpFreqDict[nuc] += 1 #increase the value
    return tmpFreqDict