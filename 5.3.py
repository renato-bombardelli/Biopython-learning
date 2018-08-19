#5.3 Parsing sequences from the net

#5.3.1 Parsing GenBank records from the net
from Bio import Entrez
from Bio import SeqIO

#FASTA
Entrez.email = "A.N.Other@example.com"
with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="6273291") as handle:
	seq_record = SeqIO.read(handle, "fasta")
print(f'{seq_record.id} with {len(seq_record.features)} features')

#GenBank
Entrez.email = "A.N.Other@example.com"
with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="6273291") as handle:
	seq_record = SeqIO.read(handle, "gb")
print(f'{seq_record.id} with {len(seq_record.features)} features')
