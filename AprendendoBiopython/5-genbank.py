from Bio import SeqIO

for seq_record in SeqIO.parse("NC_009934.gbk","genbank"):
    print(seq_record.id)
    print(seq_record.seq)
    print(len(seq_record))

    #Analisando arquivos no formato genbank e imprimindo id, a sequencia e o tamanho da sequencia.