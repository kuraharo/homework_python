def func(chisla):
    stack = []
    for chislo in chisla:
        if chislo in ("+","-","/","*"):
            b = stack.pop()
            a = stack.pop()
            if(chislo=="+"):
                c=a+b 
            elif chislo=="-":
                c=a-b
            elif chislo=="/":
                c=a//b 
            else:
                c=a*b
            stack.append(c)
        else:
            stack.append(int(chislo))
    return stack[0]
vvod = ["3", "5", "+"]
vvod = ["2", "1", "+", "3", "*"]
vvod = ["4", "13", "5", "/", "+"]
vvod=input().split()
print(func(vvod))
