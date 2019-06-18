# cook your dish here
t=int(input())
for tc in range(t):
    n=int(input())
    arr=list(input())
    for i in range(n):
        if arr[i]=="Y":
            flag=1
            break
        elif arr[i]=="I":
            flag=2
            break
        else:
            flag=0
    if flag==1:
        print ("NOT INDIAN")
    elif flag==2:  
        print ("INDIAN")
    else:
        print ("NOT SURE")
        
        
