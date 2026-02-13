n,h= list(map(int,input().split()))
m= list(map(int,input().split()))
result =0
for i in range (n):
  if m[i] <= h:
    result += 1
  else:
    result +=2 
print(result)
