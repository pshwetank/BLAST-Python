# BLAST-Python
Implementation of BLAST(Basic Local Alignment Search Tool) algorithm in Python 3.5 using Numpy. 
</br>
This code can provide you with a glimpse of how BLAST works and how it can actually be realised in code. 
</br>
This BLAST search is based on nucleotide-nucleotide search. Amino acid search using PAM scoring matrices will soon be provided on this repository.
</br>
Sorry for lack of comments in the source code. This change will also be done soon.

# File-Description:
hsp.py : Actual file with the code.
</br>word.py : File with the code implementing only w-mers fragmentation part.
</br>query.txt : File consisting of dummy sequence of E.Coli genome.
</br>assembly.txt : File consisting of database sequence of a part of E.Coli genome. As this algorithm has a time complexity of o(n^2), it is not possible to run a database search of actual genomic sequence.
