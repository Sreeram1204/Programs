a=int(input())
q=[]
b=[]
for i in range(0,a):
    p=list(map(str,input().split()))
    b.append(p)
for i in range(0,a):
    c=0
    for j in range(0,a):
        
        if b[j][i]=='C':
            c=c+1
   
    q.append(c)
print(max(q))
        
    
