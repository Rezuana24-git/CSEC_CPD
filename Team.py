n=int(input())
result=0
for i in range (n):
  arr=list(map(int,input().split()))
  c=arr.count(1)
  if c>= 2:
      result+=1
print(result)
