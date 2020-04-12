from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

      #--------PROCESSO DE TRANSCRIÇÂO----------
dna = Seq("ATGGCCATTCGCAAGGGTGCCCGATAG", \
          IUPAC.unambiguous_dna)
print("DNA: "+dna)

rna = dna.transcribe()
print("RNA: "+rna)

dna2 = rna.back_transcribe()
print("DNA2: "+dna2)