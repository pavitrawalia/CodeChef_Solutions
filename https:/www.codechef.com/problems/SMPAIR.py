# cook your dish here
t=int(input())
for tc in range(t):
    no=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(arr[0]+arr[1])
