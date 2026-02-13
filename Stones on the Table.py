n=int(input())
m=input()
cout=0
for i in range (n-1):
    if m[i] == m[i+1]:
        cout+=1
print(cout)
