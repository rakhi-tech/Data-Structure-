#Reverse the array
n = int(input("Enter the number"))
arr = [0]*n
for i in range(n):
    arr[i]= int(input("Enter the elements:"))
print("original array:",arr)
print("Array in reverse order :")
for i in range(n-1,-1,-1):
    print(arr[i],end=" ")