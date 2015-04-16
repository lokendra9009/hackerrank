#insertion_sort_1
arrlen = int(input());
arr = input();
arr_list = list(map(int,arr.split()));
num = arr_list[-1];
#print(arr_list[-1]);
n=0;
while (n<arrlen):
	if (arr_list[((arrlen-1)-n)]>=num):
		arr_list[(arrlen-1-n)]=arr_list[((arrlen-1)-(n+1))]
		print (*arr_list, sep=' ');
	else:
		arr_list[arrlen-n]=num;
	n+=1;
print (*arr_list, sep=' ');	