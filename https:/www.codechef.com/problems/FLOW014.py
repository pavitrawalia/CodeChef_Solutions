# cook your dish here

t=int(input())
for tc in range(t):
    arr=input().split()
    hs=float(arr[0])
    cc=float(arr[1])
    ts=float(arr[2])
    if hs>50 and cc<0.7 and ts>5600:
        print("10")
    elif hs>50 and cc<0.7:    
        print("9")
    elif cc<0.7 and ts>5600:
        print("8")
    elif hs>50 and ts>5600:
        print("7")
    elif hs>50 or cc<0.7 or ts>5600:    
        print("6")
    else:
        print("5")
