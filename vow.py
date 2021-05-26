import math
a=int(input())
b=[]
y=[1,2,3,4,5]
print(math.ceil(2.1))
for i in range(0,3):
    d=list(map(str,input().split()[:a]))
    b.append(d)
q=[]
for i in range(0,a):
    if b[0][i]=='#' and b[1][i]=='#' and b[2][i]=='#':
        q.append('#')
    elif b[0][i]=='.' and b[1][i]=='.' and b[2][i]=='.':
        continue;
    elif b[0][i]=='.' and b[0][i+1]=='*' and b[0][i+2]=='.' and b[1][i]=='*' and b[1][i+1]=='*' and b[1][i+2]=='*' and b[2][i]=='*' and b[2][i+1]=='.' and b[2][i+2]=='*' :
        q.append('A')
print(*q,sep='')
