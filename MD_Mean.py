print("Enter Number of given data: ")
n=int(input())
Data=[]
F=[]
X=[]
sum_FMD,sum_fx,sum_f=0,0,0
print("Enter class marks: ")
Data=input().split()
print("Enter frequencies: ")
F=input().split()
for i in range(n):
	M=int(F[i])*int(Data[i])
	print("fx= "+str(M))
	sum_fx+=M
	sum_f+=int(F[i])
print("sum_fx= "+str(sum_fx))
print("sum_f= "+str(sum_f))
print("x_bar=sum_fx/sum_f")
Mean=sum_fx/sum_f
print("x_bar= "+str(Mean))
for i in range(n):
	x=int(Data[i])-Mean
	X.append(x)
print("x - x_bar column: ")
print(X)
for i in range(n):
	FMD=int(F[i])*abs(X[i])
	print("FMD= "+str(FMD))
	sum_FMD+=FMD
print("sum_FMD= "+str(sum_FMD))
MD=sum_FMD/sum_f
print("MD_mean=sum_FMD/sum_f")
print("MD_mean= "+str(MD))
CMD=(MD/Mean)*100
print("CMD=(MD_mean/Mean)*100")
print("CMD= "+str(CMD))