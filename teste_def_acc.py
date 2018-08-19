from Bio import SeqIO

def get_acc(identifier):
	parts = identifier.split()
	return parts[0]
subjct_dict = SeqIO.index("cds.zma.fasta", "fasta", key_function=get_acc)

seq_record = subjct_dict["GRMZM5G800980"]
print(seq_record.description)
print(repr(seq_record.seq))
subjct_dict.close()