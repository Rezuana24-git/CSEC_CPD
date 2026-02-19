import math
y,w=map(int,input().split())
count=0
m=max(y,w)
for i in range(m,7):
    count+=1
s=math.gcd(count,6)
d=count//s
r=6//s
print(str(d)+'/'+str(r))
