from DNAToolkit import *
import random #random string

rndDNAStr = ''.join([random.choice(Nucleotides) #Join all items in a tuple into a string
                            for nuc in range(20)]) #loop 20
print(validateSeq(rndDNAStr))
print(countNucFrequency(rndDNAStr))
