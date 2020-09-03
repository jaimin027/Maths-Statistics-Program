print("Enter Number of given data: ")
n=int(input())
Data=[]
F=[]
sum_fx,sum_f=0,0
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
print("Mean=sum_fx/sum_f")
Mean=sum_fx/sum_f
print("Mean= "+str(Mean))
	
	