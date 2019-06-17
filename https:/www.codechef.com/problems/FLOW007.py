# cook your dish here
t=int(input())
for tc in range(t):
    no=int(input())
    rev=0
    while(no!=0):
        rev=rev*10+no%10
        
        no=no//10
    print(rev)
