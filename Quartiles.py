print("Enter Number of given data: ")
n=int(input())
Data=[]
F=[]
cf=[]
M,sum_f=0,0
print("Enter Upper limit of class: ")
Data=input().split()
print("Enter frequencies: ")
F=input().split()
for i in range(n):
	M+=int(F[i])
	cf.append(M)
	sum_f+=int(F[i])
print("cum_freqs are: ")
print(cf)
print("N= "+str(sum_f))
N=sum_f
n_by_4=N/4
n2_by_4=2*(N/4)
n3_by_4=3*(N/4)
print("N/4= "+str(n_by_4))
print("2N/4= "+str(n2_by_4))
print("3N/4= "+str(n3_by_4))
for i in range(n):
	if(n_by_4<cf[i]):
		med_f=int(F[i])
		cum_f=cf[i-1]
		med_class=int(Data[i])
		break
print("For Q1:")
print("med_f= "+str(med_f))
print("cum_f= "+str(cum_f))
h=int(Data[1])-int(Data[0])
print("h= "+str(h))
m=med_class-h
print("med_class= "+str(m) +"-"+str(med_class))
Q1=m+(n_by_4-cum_f)*(h/med_f)
print("Q1=L1+(N/4-cf)*(h/f)")
print("Q1= "+str(Q1))
for i in range(n):
	if(n2_by_4<cf[i]):
		med_f=int(F[i])
		cum_f=cf[i-1]
		med_class=int(Data[i])
		break
print("For Q2:")
print("med_f= "+str(med_f))
print("cum_f= "+str(cum_f))
h=int(Data[1])-int(Data[0])
m=med_class-h
print("med_class= "+str(m) +"-"+str(med_class))
Q2=m+(n2_by_4-cum_f)*(h/med_f)
print("Q2=L1+(2N/4-cf)*(h/f)")
print("Q2= "+str(Q2))
for i in range(n):
	if(n3_by_4<cf[i]):
		med_f=int(F[i])
		cum_f=cf[i-1]
		med_class=int(Data[i])
		break
print("For Q3:")
print("med_f= "+str(med_f))
print("cum_f= "+str(cum_f))
h=int(Data[1])-int(Data[0])
m=med_class-h
print("med_class= "+str(m) +"-"+str(med_class))
Q3=m+(n3_by_4-cum_f)*(h/med_f)
print("Q3=L1+(3N/4-cf)*(h/f)")
print("Q3= "+str(Q3))
print("QD=(Q3-Q1)/2")
QD=(Q3-Q1)/2
print("QD= "+str(QD))
print("CQD=(Q3-Q1)/(Q3+Q1)")
CMD=(Q3-Q1)/(Q3+Q1)
print("CQD= "+str(CMD))