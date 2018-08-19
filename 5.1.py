from Bio import SeqIO
'''
with open("ls_orchid.fasta") as handle:
	for seq_record in SeqIO.parse(handle, "fasta"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))
'''
#5.1.2 Iterating over the records in a sequence file
'''
first_record = next(SeqIO.parse("ls_orchid.fasta", "fasta"))
print(first_record)
'''

#5.1.3 Getting a list of records in a sequence file
'''
records = list(SeqIO.parse("ls_orchid.fasta", "fasta"))

#print("Found %i records" % len(records)) #Old syntax
print(f"Found {len(records)} records")

print("The last record")
last_record = records[-1] #using Python's list trick
print(last_record.id)
print(repr(last_record.seq))
print(len(last_record))

print("The first record")
first_record = records[0]
print(first_record.id)
print(repr(first_record.seq))
print(len(first_record))
'''

#5.1.4 Extracting data
#genbank files -> better for this type of information
'''all_species = []
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
	all_species.append(seq_record.annotations["organism"])
print(all_species)'''

#fasta files
'''all_species = []
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
	all_species.append(seq_record.description.split()[1]) #Because the specie name is in the second position (2º word) of the desciption
print(all_species)'''


