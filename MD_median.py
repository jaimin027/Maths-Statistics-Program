print("Enter Number of given data: ")
n=int(input())
Data=[]
F=[]
cf=[]
X=[]
M,sum_f,sum_FMD=0,0,0
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
n_by_2=N/2
print("N/2= "+str(n_by_2))
for i in range(n):
	if(n_by_2<cf[i]):
		med_f=int(F[i])
		cum_f=cf[i-1]
		med_class=int(Data[i])
		break
print("med_f= "+str(med_f))
print("cum_f= "+str(cum_f))
h=int(Data[1])-int(Data[0])
m=med_class-h
print("med_class= "+str(m) +"-"+str(med_class))
Median=m+(n_by_2-cum_f)*(h/med_f)
print("Median=L1+(N/2-cf)*(h/f)")
print("Median= "+str(Median))
for i in range(n):
	x=int(Data[i])-int(h/2)-Median
	X.append(x)
print("x - x_bar column: ")
print(X)
for i in range(n):
	FMD=int(F[i])*abs(X[i])
	print("FMD= "+str(FMD))
	sum_FMD+=FMD
print("sum_FMD= "+str(sum_FMD))
MD=sum_FMD/sum_f
print("MD_median=sum_FMD/sum_f")
print("MD_median= "+str(MD))
CMD=(MD/Median)*100
print("CMD=(MD_median/Mean)*100")
print("CMD= "+str(CMD))