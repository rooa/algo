"""
Calculates the nDCG value of a set of document.
nDCG is an abbreviation for "normalized Discounted Cumulative Gain".


"""


from math import log

R = 10
proportion = {"highly_relevant":2,"relevant":3,"partially_relevant":5}

n = 5
Gain = {"highly_relevant":7,"relevant":3,"partially_relevant":1,"nonrelevant":0}
retrieved_a = ["highly_relevant","highly_relevant","nonrelevant","relevant","nonrelevant"]
retrieved_b = ["partially_relevant","partially_relevant","nonrelevant","partially_relevant","nonrelevant"]

def nDCG(prop,gain,ranked_list,n):
	if n != len(ranked_list):
		raise Error

	num = 0
	denom = 0

	# calculating numerator
	for i in range(1,n+1):
		relevance = ranked_list[i-1]
		num += gain[relevance] / log(i + 1)

	# calculating denominator
	total_doc = 0
	for k,v in reversed(sorted(gain.items(),key=lambda x:x[1])):
		j = prop[k]
		for i in range(j):
			total_doc += 1
			if total_doc > n:
				print "numerator",num
				print "denominator",denom
				return num / denom
			denom += gain[k] / log((total_doc) + 1)


if __name__ == '__main__':
	print nDCG(proportion,Gain,retrieved_b, n)
