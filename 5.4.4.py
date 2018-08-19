# 5.4.4 Indexing compressed files

from Bio import SeqIO

orchid_dict = SeqIO.index_db("ls.orchid.gbk.bgz.idx", "ls_orchid.gbk.bgz", "genbank")
print(len(orchid_dict))

orchid_dict.close()
