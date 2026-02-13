n =int(input())
w=input()
a=w.count("A")
d=w.count("D")
if a==d:
  print( "Friendship")
elif a>d:
  print("Anton")
else:
  print("Danik")
