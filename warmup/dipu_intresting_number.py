#Dipu and Interesting Numbers
num = int(input())
i=2;
is_prime = True;
while (i<num):
	if (num%i==0):
		is_prime=False;
	i+=1;
if (is_prime==False):
	print("Not Prime");
else:
	print("Is Prime");