l,d=input().split( )
x=int(l)
y=int(d)
for num in range(x,y):
	power=len(str(num))
	sum=0
	temp=num
	while temp>0:
		digit=temp%10
		sum=sum+digit**power
		temp//=10
	if num==sum:
		print(num)
