l=[1,2,3,4]
def rotate(l,n):
    return l[n:]+l[:n]
print("The initial list is : ",l)
print("Enter how many times you want to left shift the list: ")
n=int(input())
L=rotate(l,n)
print("The shifted list is ",L)





    
