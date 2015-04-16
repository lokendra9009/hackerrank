inp = list();
full_string = list();
n=int(input());
for n in range(0,n):
	fstring = str(input());
	m=list(fstring);
	full_string.append(m);
#print(full_string[0][1]);
k=0
pair = 0;
while (k<len(full_string)):
	l=0;
	while (l<len(full_string[k])):
		o=l+1;
		while (o<len(full_string[k])):
			if (full_string[k][l]==full_string[k][o]):
				pair++
			o+=1;
		l+=1;
	k+=1;
	if (pair==int((len(full_string[k][l]))/2):
		res.append(0);
		pass
