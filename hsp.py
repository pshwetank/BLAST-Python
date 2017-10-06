import numpy as np
dna = open("e.coli/assembly.txt")
query = open("query.txt")

gene = []
query_seq = []
words_seq = []
hsp_word = []
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

#print(len(gene))
#print(gene)
#print(len(query_seq))

for i in range(0,len(query_seq)):
	if i+11	< len(query_seq):
		words_seq.append(query_seq[i:i+12])
#print(len(words_seq))
#print(words_seq[0][3])

def hsp():
	global hsp_word
	score = 0
	for i in range(0,len(words_seq)):
		k = 0
		score_init = 0
		index = 0
		while(len(gene) >= k+12):
			score = 0
			for j in range(k,k+12):
				if words_seq[i][j-k] == gene[j]:
					score += 5
				if words_seq[i][j-k] != gene[j]:
					score -= 4
			if score > score_init:
				score_init = score
				index = k
				#print(score_init)
			k = k+1
		hsp_word.append([score_init,i,index])

hsp()
arr = np.array(hsp_word,dtype = int)
#print(hsp_word)

def thres():
	global ref
	global thres_max
	thres_max = []
	ref = arr.max(axis=0)[0]
	for i in range(0,len(hsp_word)):
		cur_score = 0
		if arr[i][0] == ref:
			up = int(arr[i][1])
			up_left = len(query_seq)-up-12
			for j in range(up,-1,-1):
				if query_seq[j] == gene[int(int(arr[i][2])+ j - up)]:
					cur_score += 5
				if query_seq[j] != gene[int(int(arr[i][2])+ j - up)] :
					cur_score -= 4
			for k in range(up+12,len(query_seq)) :
				if query_seq[k] == gene[int((int(arr[i][2])+12)+k - up - 12)] :
					cur_score += 5
				if query_seq[k] != gene[int((int(arr[i][2])+12)+k - up - 12)] :
					cur_score -= 4	
			thres_max.append([cur_score,i])		



	#for i in range()
thres()
#print(thres_max)
def disp():
	for i in range(0,len(thres_max)):
		print("Query:")
		print(words_seq[int(thres_max[i][1])])
		print("Sequence:")
		print(gene[int(hsp_word[int(thres_max[i][1])][2]) : int(hsp_word[int(thres_max[i][1])][2])+12])
		print()
#disp()
#print(ref)
def dispx():
	for i in range(0,len(thres_max)):
		print("Query:")
		print(''.join(map(str,query_seq[0:len(query_seq)-1])))
		print("Sequence:")
		print(gene[int(hsp_word[int(thres_max[i][1])][2]) : int(hsp_word[int(thres_max[i][1])][2])+12])
		print()
dispx()

dna.close()
query.close()
