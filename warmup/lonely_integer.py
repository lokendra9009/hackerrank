#lonely_integer
from collections import Counter
no_of_inp = int(input());
inp_num = input();
arr_inp = list(map(int,inp_num.split(" ")));
is_single=0;
num_count=Counter(arr_inp);
print(num_count.items())
#print(num_count.values())
for key,value in num_count.items():
	if (value==1):
		print(key);

