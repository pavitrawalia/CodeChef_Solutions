# cook your dish here
t=int(input())
for tc in range(t):
    str1=input()
    str2=input()
    count=0
    for i in range(len(str1)):
        if str1[i]!=str2[i] and str1[i]!="?" and str2[i]!="?":
            count+=1
    if count==0:
        print("Yes")
    else:
        print("No")
