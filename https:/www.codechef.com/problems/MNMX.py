# cook your dish here
t=int(input())
for tc in range(t):
    l=int(input())
    arr=sorted(map(int,input().strip().split(' ')))
    sum1=arr[0]*(l-1)
    print(sum1)   
