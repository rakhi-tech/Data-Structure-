#wite a program to acccept N intergers into an array and calculate and display the sum of all elements
n = int(input("enter the number:"))
arr =[]

for i in range(n):
    num = int(input("enter the elements"))
    arr.append(num)
    sum=0
for i in range(n):
    sum = sum +arr[i]
print("the some of elements",sum)