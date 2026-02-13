n=int(input())
per=""
group=0
for i in range (n):
    m=input()
    if m != per:
        group+=1
    per = m
print(group)
