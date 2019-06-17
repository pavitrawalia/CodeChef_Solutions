# cook your dish here
t=int(input())
for tc in range(t):
    no1=int(input())
    no2=no1
    sum=0
    while(no2!=0):
        sum=sum*10+no2%10
        no2//=10
    
    if no1==sum:
        print("wins")
    else:
        print("losses")
        
