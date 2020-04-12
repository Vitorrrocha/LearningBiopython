from Bio import SeqIO
exemplo = SeqIO.read("NC_009934.gbk","genbank")
for i in exemplo.features:  #Features são campos onde são armazenadas algumas caracteristicas do organismo.
    if(i.type=="CDS"):
        print(i.qualifiers['product'])

#Obtendo nome de produtos codificados de um arquivo genbank