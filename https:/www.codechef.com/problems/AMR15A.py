# cook your dish here
n=int(input())
arr=list(int(x) for x in input().split())
counte=counto=0
for j in range(n):
    if arr[j]%2==0:
        counte+=1
    else:
        counto+=1
if counte>counto:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
