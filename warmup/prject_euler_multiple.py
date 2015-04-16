#Project Euler #1: Multiples of 3 and 5

num_of_inp = int(input());
inp = list();
n=0;
while (n<num_of_inp):
	inp.append(int(input()));
	n=n+1;
	pass
print(len(inp));
res = 0;
while (res<num_of_inp):
	print(inp[res]);
	res=res+1;
	pass