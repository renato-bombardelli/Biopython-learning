from Bio import SeqIO
'''
orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.gbk", "genbank"))

#print(len(orchid_dict))

seq_record = orchid_dict["Z78475.1"]
print(seq_record.description)
print(seq_record.id)
print(seq_record.seq)
'''

#FASTA

def get_accession(record):
	parts = record.id.split("|")
	return parts[3]


orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.fasta", "fasta"), key_function=get_accession)

print(orchid_dict.keys())
