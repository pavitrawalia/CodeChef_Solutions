# cook your dish here

t=int(input())
for tc in range(t):
    b_sal=int(input())
    if b_sal<1500:
        g_sal=b_sal*2
    else:
        g_sal=b_sal+500+0.98*b_sal
        
    print(g_sal)        
