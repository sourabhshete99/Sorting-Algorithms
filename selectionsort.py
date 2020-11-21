#	sorting an array/list of numbers/int by Selection sort method

num=list(map(int,input("\n Enter numbers :").split()))
l=len(num)

for i in range(0,l):
	m=int(-1)
	temp=None
	
	# find for max element from list
	for j in range(0,l-i):
		if num[j]>m:
			m=num[j]
			maxindex=j
			
	#swap it to the last position
	temp=num[maxindex]
	num[maxindex]=num[l-i-1]
	num[l-i-1]=temp
	
print(num)
