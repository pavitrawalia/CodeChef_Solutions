# cook your dish here
t=int(input())
for tc in range(t):
    (n,s)=map(int,input().split())
    sum1=0
    for i in range(1,n+1):
        for j in range(1,s+1):
            sum1+=j
        s=sum1
        if i==n:
            pass
        else:
            sum1=0
    print(sum1)        
