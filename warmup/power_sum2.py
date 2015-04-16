inp = int(input());
res = list();
num=(inp**inp)

print (num)

while True:
	if (num<10):
			break;
	else:
		res.append(num%10);
		num=int(num/10);
		print("quotient ="+str(num));
res.append(num);
print (res);
print (sum(res));