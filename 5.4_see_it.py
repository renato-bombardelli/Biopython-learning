#5.4 Sequence files as Dictionaries
	# Bio.SeqIO.to_dict() -> high memory usage, but most flexible
	# Bio.SeqIO.index() -> middle ground
	# Bio.SeqIO.index_db() -> low memory, but a little bit slower

from Bio import SeqIO

## 5.4.1 Sequence files as Dictionaries - In memory

'''
orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.gbk", "genbank"))
#print(list(orchid_dict.keys()))
#print(list(orchid_dict.values()))

seq_record = orchid_dict["Z78475.1"]
#print(seq_record.description)
#print(repr(seq_record.seq))
'''

# 5.4.1.1 Specifying the dictionary keys
'''
orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.fasta", "fasta"))
#print(orchid_dict.keys())
#print(orchid_dict.values())

#define a function to cat the gene ID in fasta files by its record
def get_accession(record):
	parts = record.id.split("|")
	assert len(parts) == 5 and parts[0] == "gi" and parts[2] == "emb"
	return parts[3]

orchid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.fasta", "fasta"), key_function=get_accession)
print(orchid_dict.keys())
'''

# 5.4.1.2 Indexing a dictionary using the SEGUID checksum
'''
from Bio.SeqUtils.CheckSum import seguid

#for record in SeqIO.parse("ls_orchid.gbk", "genbank"):
#	print(record.id, seguid(record.seq))

seguid_dict = SeqIO.to_dict(SeqIO.parse("ls_orchid.gbk", "genbank"), lambda rec : seguid(rec.seq))
record = seguid_dict["MN/s0q9zDoCVEEc+k/IFwCNF2pY"]
print(record.id)
print(record.description)
'''
## 5.4.2 Sequence files as Dictionaries - Index files (middle ground)

'''
orchid_dict = SeqIO.index("ls_orchid.gbk", "genbank")
print(len(orchid_dict))
print(orchid_dict.keys())
#seq_record = orchid_dict["Z78475.1"]
#print(seq_record.description)
#print(repr(seq_record.seq))
orchid_dict.close()
'''

#5.4.2.1 Specifying the dictionary keys

'''
def get_acc(identifier):
	parts = identifier.split("|")
	assert len(parts) == 5 and parts[0] == "gi" and parts[2] == "emb"
	return parts[3]
orchid_dict = SeqIO.index("ls_orchid.fasta", "fasta", key_function=get_acc)
print(orchid_dict.keys())

seq_record = orchid_dict["Z78475.1"]
print(seq_record.description)
print(repr(seq_record.seq))
orchid_dict.close()
'''

# 5.4.2.2 Getting the raw data for a record
'''hmmmmm'''

#######################################
## 5.4.3 Sequence files as Dictionaries - Database index files (index_db())


