n=int(input())
for i in range(n):
  a,b=map(int,input().split())
  m=a%b
  if m==0:
    moves=0
  else:
      moves=b-m
  print(moves)
