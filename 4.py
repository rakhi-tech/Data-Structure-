#search an element
n = int(input("Enter the number:"))
arr = [0]*n
for i in range(n):
    arr[i]=int(input("Enter the elements:"))
search= int(input("enter the number for search:"))
found = False
for i in range(n):
    if arr[i]== search:
        print("Number is present at position:",i + 1)
        found = True
        break
    if found == False:
     print("Number is not present in the array")