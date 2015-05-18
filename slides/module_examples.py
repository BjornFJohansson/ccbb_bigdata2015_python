# SJS
# Script to demonstrate sys, and possibly others


import sys
#from sys import path
#from sys import *

#print sys.path
#print sys.argv

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

seq = Seq("ACGTC")
#print dir(seq)

seqrec = SeqRecord(seq)

#print seqrec

# Defining a SeqRecord object
#seq_object = Seq("ACGTC")
#seq_record = SeqRecord(seq_object, id = "my_id", description="")

#SeqIO.write(seq_record, "outfile.fasta", "fasta")


recs = []
for i in range(10):
	seq_object = Seq("ACGTA")
	seq_record = SeqRecord(seq_object, id = "id" + str(i))
	recs.append(seq_record)

SeqIO.write(recs, "outfile.fasta", "fasta")
