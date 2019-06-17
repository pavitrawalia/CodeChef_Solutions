# cook your dish here
t=int(input())
for tc in range(t):
    (val1,val2)=map(int,input().split())
    if val1<val2:
        print("<")
    elif val2<val1:
        print(">")
    else:
        print("=")
