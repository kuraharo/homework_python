a=input()
b=((len(a)+3)//2-1)
c=len(a)//2-1

if(a[:b:] == a[:c:-1]):
   print("palidrom")
else:
   print("ne palidrom")

#print(a[:b:])
#print(a[:c:-1])