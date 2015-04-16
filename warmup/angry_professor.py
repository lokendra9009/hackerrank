#angry_professor
no_of_tc = int(input());
res = []
for a in range(0,no_of_tc):
	student=str(input());
	stu_time=[];
	on_time = 0;
	stu_count = list(map(int,student.split(" ")));
#print (stu_count);
	time = str(input());
	stu_time = list(map(int,time.split(" ")));
#print(stu_time);
	for x in range(0,len(stu_time)):
		if (stu_time[x]<=0):
			on_time+=1;
		#print (on_time);
	if (on_time>=stu_count[-1]):
		res.append("NO");		
	else:
		res.append("YES");
print(*res,sep='\n');