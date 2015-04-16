tc = input("Enter the number of times you want to provide inputs : ");

inp = list();
for tc in range(int(tc)):						#For getting the input range
	
	inp.append(int(input("Number : ")))         # Gets the inputs
res = 0
for res in range(0,tc+1):
	print(inp[res]);


