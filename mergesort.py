#	sorting an array/list of numbers/int by Merge sort method

def merge(num):
	if len(num)>1:
		m=len(num)//2
		L=num[:m]
		R=num[m:]

		merge(L)
		merge(R)
	
		i=j=k=0
		# merging two into one
		while i<len(L) and j<len(R):
			if L[i]<R[j]:
				num[k]=L[i]
				i+=1
			else:
				num[k]=R[j]
				j+=1
			k+=1		
		# merging the remaining elements
		while i < len(L):
			num[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			num[k] = R[j]
			j += 1
			k+=1
	
num=list(map(int,input("\n Enter numbers :").split()))
merge(num)

print(num)

