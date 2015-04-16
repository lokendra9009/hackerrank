tc = int(input());
total_comb = 0
if (tc>=1 and tc<=100):
	n=1;
	res = list();
	while (n<=tc):
		min = 0;
		max = 0;
		range_num = list(map(int, input.split()));
		print (range_num)
		min = int(min);
		max = int(max);
		if (min>6):
			res.append("YES");
		else:
			k = min;
			while (k<=max):
				total_comb=total_comb+(10**k);
				k+=1;
			if (total_comb>(10**6)):
				res.append("YES");
			else:
				res.append("NO");
		n=n+1;	
	m=0;
	print '\n'.join([ str(myelement) for myelement in res ])