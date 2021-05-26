a,b=map(int,input().split(','))
d=[]
for i in range(1,a+1):
    if  a%i==0:
        if i not in d:
            d.append(i)
print(d)
if len(d)>=b:
    print(d[b])
else:
    print(1)
