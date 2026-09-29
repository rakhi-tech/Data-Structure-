#removing duplicates in an array
n = int(input("Enter the number"))
arr = [0]*n
for i in range(n):
    arr[i]=int(input("the the elements:"))
unique = []
for i in range(n):
    if arr[i] not in unique:
        unique.append(arr[i])
print("original array:",arr)
print("Array after removing the duplicates:",unique)
    

