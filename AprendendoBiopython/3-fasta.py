from Bio import SeqIO
for i in SeqIO.parse("arquivo.fasta","fasta"):
    print(i.id)
    print(i.seq)
    print(len(i))

# Fizemos a leitura dos dados do arquivo: "arquivo.fasta" e imprimos algumas informações.