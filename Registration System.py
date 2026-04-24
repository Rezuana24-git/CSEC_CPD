n=int(input())
dict={}
for i in range(n):
    name=input()
    if name not in dict:
        print("OK")
        dict[name]=1 
    else:
        print(name + str(dict[name]))
        dict[name]+=1
