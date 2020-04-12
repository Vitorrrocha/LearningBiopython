from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

     #--------PROCESSO DE TRADUÇÂO--------------
rna = Seq("AUGGCCAUUCGCAAGGGUGCCCGAUAG", \
          IUPAC.unambiguous_rna)
proteina_rna = rna.translate()
print(proteina_rna)

dna = Seq("ATGGCCATTCGCAAGGGTGCCCGATAG", \
          IUPAC.unambiguous_dna)
proteina_dna = dna.translate()
print(proteina_dna)
