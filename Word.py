s=input()
u=0
l=0
for ch in s:
  if ch.isupper():
    u+=1
  elif ch.islower():
    l+=1
if u == l or l>u:
  print(s.lower())
else:
  print(s.upper())
