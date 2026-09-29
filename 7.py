#moving the zeroes
n = int(input("Enter the numer:"))
arr = [0]*n
for i in range(n):
    arr[i]=int(input("enter the elements:"))
j=0
for i in range(n):
    if arr[i]!=0:
        arr[j]=arr[i]
        j=j+1
while j < n:
    arr[j]=0
    j=j+1
print("Array after moving zeroes to the end :",arr)