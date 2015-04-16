#Find Digits
import itertools
no_of_tc = int(input());
res = [];
count = 0;
for x in range(0,no_of_tc):
	num=int(input());
	num_str = str(abs(num));
	count=0;
	for y in range(0,len(num_str)):
		if (int(num_str[y])!=0):
			if(num%(int(num_str[y]))==0):
				count+=1;
	res.append(count)
print(*res,sep="\n")