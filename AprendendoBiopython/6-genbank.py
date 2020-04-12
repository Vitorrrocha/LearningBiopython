from Bio import SeqIO
#Recebendo arquivo bgk
exemplo = SeqIO.read("NC_009934.gbk","genbank")
for i in exemplo.features:
    print(i)


# Imprimindo todas as features de um arquivo genbank