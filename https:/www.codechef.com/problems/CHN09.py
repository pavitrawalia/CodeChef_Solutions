# python is no allowed language to solve this problem on codechef :)
#but still the solution goes like this 
t=int(input())
for tc in range(t):
    s=input()
    counta=countb=0
    for i in range(len(s)):
        if s[i]=="a":
            counta+=1
        else:
            countb+=1
    if counta>countb:
        print(countb)
    else:
        print(counta)
