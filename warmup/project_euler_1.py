#Project Euler #1: Multiples of 3 and 5

tc = abs(input());
inp = list();
is_multiple = list();
n=0;
while (n<tc and tc>=1 and tc <=(10**5)):
	inp.append(abs(input()));
	n=n+1;
m=0;
while (m<tc):
	num=1;
	while (num<inp[m] and inp[m]>=1 and inp[m]<=(10**9)):
		if(num%3==0 or num%5==0):
			is_multiple.append(num);
		num=num+1;
	print(sum(is_multiple));
	del is_multiple[:];
	m=m+1;


