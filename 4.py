a=input()
i=0
while(1):
    if(len(a)==0):
        print("true")
        exit()
    if(a[i]+a[i+1]=='()' or a[i]+a[i+1]=='[]' or a[i]+a[i+1]=='{}'):
        a=a[:i]+a[i+2:]
        i=0
    else:
        if(len(a)!=0 and i+1==len(a)-1):
            print("false")
            exit()
        i+=1