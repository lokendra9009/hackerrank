#Lonely Integer

#!/usr/bin/py
# Head ends here
answer = list();
number_of_tc = int(input("Enter the number of test cases :"));
print (number_of_tc);
inp = raw_input();
print (inp);
print len(inp);
if (len(inp)==(number_of_tc+(number_of_tc-1))):
	inp_split = map(int, inp.split())
	print (inp_split);
	print (len(inp_split));
	n=0;
	while (n<number_of_tc):
		m=0;
		while (m<number_of_tc):
			if (inp_split[n]==inp_split[m] and m!=n):
				break;
			else:
				answer.append(inp_split[n]);					
			m=m+1;
		n=n+1;
	print(answer);
	#print(inp_split[3]);
else:
	print("Lenth of input should not be more than "+str(number_of_tc)+" inputs");