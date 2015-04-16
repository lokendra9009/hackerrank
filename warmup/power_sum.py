#Project Euler #56: Powerful digit sum
inp = list();
inp_sum = list();
res_sum = list();
num = int(input());
a=1;
b=1;
if (num>=5 or num<=200):
	while (a<=num):
		#print("a = "+str(a));
		b=1;
		while (b<=num):
			#print("b="+str(b));
			inp.append(a**b);
			#print("power = "+str(a**b));
			b+=1;	
		a+=1;
#print (inp);
i=0;
q = 1;
while (i<len(inp)):
	q=inp[i];
	#print ("\n"+str(q));
	del inp_sum[:];
	while True:
		if (q<10):
			break;
		else:
			inp_sum.append(q%10);
			q=int(q/10);
			#print("quotient ="+str(q));
	inp_sum.append(q);
	res_sum.append(sum(inp_sum));
	i=i+1;
	#print(inp_sum);
print (max(res_sum));			
#inp.append(n);
#print (sum(inp));


