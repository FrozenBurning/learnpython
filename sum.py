
a=int(input("please input a:"))
n=int(input("please input n:"))
sum=0

for i in range(1,n+1):
    sum=sum+a*(10**(i-1))*(n-i+1)
    
print("the sum is:",sum)
