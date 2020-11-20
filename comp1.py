
print("The inital list is: ")
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(l)
print("Enter the number you want to add to the list: ")
n=int(input())
print("Enter the position you want to add to the number: ")
pos=int(input())
p=pos-1
l.insert(p,n)
print("The updated list is: ")
print(l)
        
