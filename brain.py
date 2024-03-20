import random
i=10
wrongs=0
while i>0:
	a=random.randrange(1,10)
	b=random.randrange(1,10)
	c=a+b
	print(a,"+",b)
	x=int(input())
	if x==c:
		print("correct!")
	if x!=c:
		print("wrong!")
		wrongs+=1
	i-=1
	if i==0:
		print("you got",wrongs,"wrongs")
	if i==0 and  wrongs==0:
		print("congrats!")