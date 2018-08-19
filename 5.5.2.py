#5.5.2 Converting between sequence file formats

from Bio import SeqIO
records = SeqIO.parse("ls_orchid.gbk", "genbank")
count = SeqIO.write(records, "my_convertion_Ex.fasta", "fasta")
print(f'Converted {count} records')

#or simply

count = SeqIO.convert("ls_orchid.gbk", "genbank", "My_Convertion_example.fasta", "fasta")
print(f'Converted {count} records')
