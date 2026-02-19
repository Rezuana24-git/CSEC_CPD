s=input()
t=input()
pos=0
for i in range(len(t)):
    if s[pos]==t[i]:
        pos+=1
print(pos + 1)
