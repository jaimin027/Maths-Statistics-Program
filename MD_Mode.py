print("Enter Number of given data: ")
n=int(input())
Data=[]
F=[]
X=[]
sum_f,sum_FMD=0,0
print("Enter Upper limit of class: ")
Data=input().split()
print("Enter frequencies: ")
F=input().split()
for i in range(n):
	F[i]=int(F[i])
	sum_f+=F[i]
print("sum_f= "+str(sum_f))
fm=max(F)
h=int(Data[1])-int(Data[0])
for i in range(n):
	if(fm==int(F[i])):
		f1=int(F[i-1])
		f2=int(F[i+1])
		UC=int(Data[i])
LC=UC-h
print("fm= "+str(fm))
print("f1= "+str(f1))
print("f2= "+str(f2))
print("h= "+str(h))
print("mode_class= "+str(LC)+"-"+str(UC))
print("Mode=L1+((fm-f1)/(2fm-f1-f2))*h")
Mode=LC+((fm-f1)/(2*fm-f1-f2))*h
print("Mode= "+str(Mode))
for i in range(n):
	x=int(Data[i])-int(h/2)-Mode
	X.append(x)
print("x - x_bar column: ")
print(X)
for i in range(n):
	FMD=int(F[i])*abs(X[i])
	print("FMD= "+str(FMD))
	sum_FMD+=FMD
print("sum_FMD= "+str(sum_FMD))
MD=sum_FMD/sum_f
print("MD_mode=sum_FMD/sum_f")
print("MD_mode= "+str(MD))
CMD=(MD/Mode)*100
print("CMD=(MD_mode/Mode)*100")
print("CMD= "+str(CMD))