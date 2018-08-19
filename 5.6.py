# 5.6 Low level FASTA and FASTAQ parsers

from Bio.SeqIO.FastaIO import SimpleFastaParser

count = total_len = 0
with open("ls_orchid.fasta") as in_handle:
	for title, seq in SimpleFastaParser(in_handle):
		count += 1
		total_len += len(seq)
print(f'{count} records with total sequence length {total_len}')

#???# out_handle.write('>' + f'{title} \n {seq} \n')

