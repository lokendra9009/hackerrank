num = int(input());
array_len = int(input());
inp = input();
inp_array = list(inp);
print (inp_array);
n=0;
while (n<array_len):
	if (inp_array[n]==num):
		print (n);
		break;
	n+=1;
