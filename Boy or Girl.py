n=input()
s=[]
for i in n:
  if i not in s:
    s.append(i)
m=len(s)
if m%2 ==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
