from Bio import Seq
from Bio import SeqIO
import sys
import re

 

repeat = ["(gcc){4,}","(cgg){4,}","(cag){4,}","(ctg){4,}","(ccg){4,}"]
for record in SeqIO.parse(sys.argv[1], "fasta"):
  chr = record.id
  for rep in repeat:
   for match in re.finditer (rep,str (record.seq), re .IGNORECASE) :
      print chr, match.start(), match.end(),abs((match.start()-match.end())/3), match.group()
  for rep in repeat:
    for match in re.finditer(rep, str(record.seq.reverse_complement(), re .IGNORECASE)):
       print(chr, match.start(), match.end(),abs((match.start()-match.end())/3, match.group())
