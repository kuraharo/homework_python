sum=0

N=int(input())
for i in range (2,N+1):
    flag=1
    for m in range (2,i):
        if(i%m==0):
            flag=0
    if(flag==1):
        sum=sum+i
print(sum)
