n=int(input())
result=[]
for i in range(n):
  a,b=map(int,input().split())
  m=a%b
  if m==0:
    moves=0
  else:
      moves=b-m
  result.append(moves)
for m in range(len(result)):
  print(result[m])
