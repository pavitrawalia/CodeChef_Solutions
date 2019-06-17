# cook your dish here
t=int(input())
for tc in range(t):
    n=int(input())
    fact=1
    for no in range(1,n+1):
        fact=fact*no
    print (fact)    
