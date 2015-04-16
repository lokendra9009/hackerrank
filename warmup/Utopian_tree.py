tc = input();

inp = list();
for tc in range(int(tc)):						#For getting the input range
	
	inp.append(int(input()))         # Gets the inputs
res = 0
for res in range(0,tc+1):
	num = inp[res];
	year = int(num/2);
	#print (year);
	n=1;
	x_val = 1;
	for n in range(0,year):
		x_val = (2*x_val)+1;
	if (num%2)!=0:
		x_val = x_val*2;
	print (x_val);	