n = int(input("Enter the number of rows: "))
mid = n // 2   

for i in range(n):
    for j in range(n):
        if j == mid or i == mid:   
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
