#find the smallest and largest element
n = int(input("enter the elements:"))
arr = [0]*n
for i in range(n):
    arr[i]= int(input("Enter the element:"))
    largest = arr[0]
    secondlargest = arr[0]
    smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        secondlargest = largest
        largest = arr[i]
    elif arr[i]>secondlargest and arr[i]!=largest:
        secondlargest = arr[i]
    if arr[i]<smallest:
        smallest=arr[i]
print("largest element:",largest)
print("second largest element:",secondlargest)
print("smallest element:",smallest)