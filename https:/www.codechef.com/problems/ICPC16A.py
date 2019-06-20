# cook your dish here
t=int(input())
for tc in range(t):
    arr=list(map(int,input().rstrip().split()))
    if arr[0]>arr[2]:
        if arr[1]!=arr[3]:
            print("sad")
        else:
            print("left")
    elif arr[0]==arr[2]:
        if arr[1]>arr[3]:
            print("down")
        else:
            print("up")
    
    else:
        if arr[1]!=arr[3]:
            print("sad")
        else:
            print("right")
