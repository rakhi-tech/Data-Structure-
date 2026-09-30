n = 5
sp = n - 1
for i in range(1, n+1):
    # spaces
    for s in range(sp, 0, -1):
        print(" ", end="")

    for j in range(1, i+1):
        print(j, end="")
    
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()   

    
