#	sorting an array/list of numbers/int by Selection sort method

num=list(map(int,input("\n Enter numbers :").split()))
l=len(num)

for i in range(0,l-1):
	for j in range(0,l-1):
		# check the number is greater than next number, if it is then swap them
		if num[j]>num[j+1]:
			num[j],num[j+1]=num[j+1],num[j]
			# this is just like "a,b=b,a", python assigns in such way, in short it exchanges the two values
			
print(num)
