l=[1,1,21,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,71,15,16,17,18,181,918,133,144,144,18]
l.sort()
a=len(l)+1
count=1
d=max(l)
for i in range(a):
    if l[i]==d:
        break
    if l[i]==l[i+1]:
        continue
    else:
        count+=1
print(l)
print(count)
