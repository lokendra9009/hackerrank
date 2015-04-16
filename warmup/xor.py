#import pdb
l = int(input());
r = int(input());
c = 0;
#largest = c;

largenum = 0;
#c = l^r;

#print (c);

#pdb.set_trace();
x = l;
y = l;

for x in range(l,r+1):
	pass
	for y in range(x,r+1):
		c=x^y;
		y +=1;

		if (largenum<c):
			largenum = c;
x +=1;
y = x;
print(largenum);			
##c = a^b;
##print (c);
#num1 = l;
#num2 = l;
#for num1 in range(r):
#    for num2 in range(num1,r):
#        c=num1^num2;
#         
#        if (largest<c):
#            largest=c;
#        else:
#            continue;
 #       num2+=1;
#    num1+=1;
#    num2 = num1;

#print (largest);