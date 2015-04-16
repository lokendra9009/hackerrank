#dividing a string into two 

full_string = str(input());
half = len(full_string)/2;
half = int(half);
second_ascii = list();
first_ascii = list();
#print(len(full_string));
#print(half);
if ((len(full_string)%2)==0):
	firstpart = str(full_string[:half]);
	secondpart = str(full_string[half:]);
else :
	firstpart = str(full_string[:half]);
	secondpart = str(full_string[half+1:]);
#print(firstpart);
#print(secondpart);
eos = int(len(firstpart)/2);
rev_secondpart = secondpart[::-1];
#print(rev_secondpart);
#print(ord("a"));
n=0;
first_ascii = list();
rev_secondpart_ascii = list();
while (n<len(firstpart)):
	first_ascii.append(ord(firstpart[n]));
	#print(first_ascii);
	n=n+1;
m=0;
while(m<len(rev_secondpart)):
	rev_secondpart_ascii.append(ord(rev_secondpart[m]))
	m=m+1;
	#print(rev_secondpart_ascii);
k=0;
diff = list();
while (k<len(firstpart)):
	diff.append(abs(first_ascii[k]-rev_secondpart_ascii[k]));
	k=k+1;
	#print(diff);
print(sum(diff));



#for x in range():
#	pass


#print(firstpart);
#print (secondpart);