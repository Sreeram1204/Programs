n,m=map(int,input().split())
c=0
for i in range(0,n):
   a=list(input())
   b=a.count('1')
   c=c+b
print(c)
if c<4:
   print(1)
elif c>4 and c<9:
   f=2
elif c<9 and c<16:
   f=3
elif c<16 and c<25:
   f=4
elif c<25 and c<36:
   f=5


for i in range(0,f):
   d=[]
   for j in range(0,f):
      d.append(1)
   print(*d,sep=' ')
