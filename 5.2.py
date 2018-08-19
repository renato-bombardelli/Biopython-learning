#working with compact files

import gzip #module to deal(open, read) with 'gz' compact files
from Bio import SeqIO

with gzip.open("ls_orchid.gbk.gz", "rt") as handle:
	print(sum(len(r) for r in SeqIO.parse(handle, "gb")))
	#shows the total number of records in the file


import bz2 #module to deal with 'bz2' comptact files
from Bio import SeqIO

handle = bz2.open("ls_orchid.gbk.bz2", "rt")
with handle:
	print(sum(len(r) for r in SeqIO.parse(handle, "gb")))

