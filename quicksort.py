#	sorting an array/list of numbers/int by Quick sort method

num=list(map(int,input("\n Enter numbers :").split()))
l=len(num)

def part(low,high):
	p=num[high]
	i=low-1
	
	for j in range(low,high):
		if num[j]<=p:
			i+=1
			num[i],num[j]=num[j],num[i]
	
	num[i+1],num[high]=num[high],num[i+1]
	return i+1	

def quick(low,high):
	if low<high:
		pi=part(low,high)
		quick(low,pi-1)
		quick(pi+1,high)
		
quick(0,l-1)
print(num)
