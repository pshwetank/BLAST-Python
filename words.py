dna = open("e.coli/assembly.txt")
query = open("query.txt")
gene = []
query_seq = []
words_seq = []
for line in dna:
	if line[0] != '>':
		end = len(line)
		for words in line[0:end-1]:
			gene.append(words)
		
for line in query:
	if line[0] != '>':
		end = len(line)
		for words in line[0:end]:
			query_seq.append(words)

print(len(gene))
print(len(query_seq))

for i in range(0,len(query_seq)):
	if i+11	< len(query_seq):
		words_seq.append(query_seq[i:i+12])
print(len(words_seq))
print(words_seq)
dna.close()
query.close()