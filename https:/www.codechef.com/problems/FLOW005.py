# cook your dish here
# Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100
t=int(input())
for tc in range(t):
    count=0
    value=int(input())
    while(1):
        if value>=100:
            count+=1
            value=value-100
        elif value>=50:   
            count+=1
            value=value-50
        elif value>=10:   
            count+=1
            value=value-10
        elif value>=5:   
            count+=1
            value=value-5
        elif value>=2:   
            count+=1
            value=value-2
        elif value>=1:   
            count+=1
            value=value-1   
        else:
            pass
        if (value==0):
            print(count)
            break
        else:
            pass
    
