#Secure password system

tc = int(input());
if (tc>=1 and tc<=100):
	n=1;
	res = list();
	while (n<=tc):
		min = 0;
		max = 0;
		min,max = input().split();
		min = int(min);
		max = int(max);
		if(min>=1 and max<=10 and max>=min):

			if (min==max):

				total_combination = min;
			else:

				total_combination = min+max;
			if (total_combination>6):

				res.append("YES");				
			else:
				res.append("NO");	
		n=n+1;	
	m=0;
	print(*res, sep='\n');
