print("Enter Number of given data: ")
n=int(input())
Data=[]
F=[]
sum_f=0
print("Enter Upper limit of class: ")
Data=input().split()
print("Enter frequencies: ")
F=input().split()
fm=int(max(F))
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
