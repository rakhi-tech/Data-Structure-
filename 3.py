#count even and odd numbers
n = int(input("enter the number:"))
arr = [0]*n
for i in range(n):
    arr[i]=int(input("enter the elements"))
even=0
odd=0
for i in range(n):
    if arr[i]%2==0:
        even = even + 1
    else:
        odd = odd + 1
print("number of even elements:",even)
print("number of odd elements:",odd)

