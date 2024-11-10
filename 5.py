from collections import deque
first_list = deque([1,3,5,7])
second_list = deque([2,4,6,8])
third_list=deque([])
#first_list=input()
#second_list=input()
i=0
for i in range (len(first_list)+len(second_list)):
    print(str(i)+' '+str(first_list)+' '+str(second_list))
    if(len(first_list)==0 or len(second_list)==0):    #проверка, чтоб не обращаться к несуществующему элем
        if(len(first_list)==0):
            third_list=third_list+second_list
            print('otvet:'+str(third_list))
            exit()
        else:
            third_list=third_list+first_list
            print('otvet:'+str(third_list))
            exit()                                    #end check 
    if(first_list[0]<second_list[0]):
        third_list.append(first_list[0])
        first_list.popleft()
    else:
        third_list.append(second_list[0])
        second_list.popleft()
    i+=1
