# cook your dish here
t=int(input())
for tc in range(t):
    a=int(input())
    last=a%10
    while(a!=0):
        first=a%10
        a=a//10
    print(first+last)        
