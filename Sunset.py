n=int(input())
d=[]
c=[]
for i in range(0,n):
  x=int(input())
  y=list(map(int,input().split()[:x]))
  c.append(x)
  d.append(y)
e=[]
for i in range(0,n):
  s=0
  
  for j in range(0,c[i]):
    if d[i][0] is max(d[i]):
      s=s+1
      d[i].pop(0)
    else:
      d[i].pop(0)
  e.append(s)
for i in range(0,len(e)):
  print(e[i])
