# cook your dish here
t=int(input())
for tc in range(t):
    coin=[]
    (n,k)=map(int,input().split())
    for j in range(1,k+1):
        coin.append(n%j)
    print(max(coin))
