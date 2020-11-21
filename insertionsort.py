#	sorting an array/list of numbers/int by Insertion sort method

num=list(map(int,input("\n Enter numbers :").split()))
l=len(num)

for i in range(1,l):
	key=num[i]
	j=i-1
	
	while j>=0 and num[j]>key:
		num[j+1]=num[j]
		j-=1
	
	num[j+1]=key
	
print(num)
