# Vamos pegar a sequencia do arquivo "arquivo1.fasta"
# e passar o dados filtrados com oque queremos para "arquivo2.fasta"


from Bio import SeqIO
entrada = open("arquivo1.fasta","r")
saida = open("arquivo2.fasta","w")

for i in SeqIO.parse(entrada,"fasta"):
    if((len(i.seq)>10) and (i.seq[0]=="C")):
        SeqIO.write(i,saida,"fasta")
saida.close()