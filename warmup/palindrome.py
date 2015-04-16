# The Love-Letter Mystery

inp = list();
full_string = list();
n=int(input());
for n in range(0,n):
	full_string.append(str(input()));
res=0	
for res in range(0,n+1):
	#print(full_string[res]);
	half = len(full_string[res])/2;
	half = int(half);
	second_ascii = list();
	first_ascii = list();
	if ((len(full_string[res])%2)==0):
		firstpart = str(full_string[res][:half]);
		secondpart = str(full_string[res][half:]);
	else :
		firstpart = str(full_string[res][:half]);
		secondpart = str(full_string[res][half+1:]);
	eos = int(len(firstpart)/2);
	rev_secondpart = secondpart[::-1];
	n=0;
	first_ascii = list();
	rev_secondpart_ascii = list();
	while (n<len(firstpart)):
		first_ascii.append(ord(firstpart[n]));
		n=n+1;
	m=0;
	while(m<len(rev_secondpart)):
		rev_secondpart_ascii.append(ord(rev_secondpart[m]))
		m=m+1;
	k=0;
	diff = list();
	while (k<len(firstpart)):
		diff.append(abs(first_ascii[k]-rev_secondpart_ascii[k]));
		k=k+1;
	print(diff);
	print(sum(diff));	

