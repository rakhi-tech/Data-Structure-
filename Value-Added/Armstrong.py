
def isArmstrong(n):
    # Count digits
    num_digits = 0
    temp = n
    while temp > 0:
        num_digits += 1
        temp //= 10

    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    
    return total == n


print(isArmstrong(153))   
print(isArmstrong(12))    
print(isArmstrong(9474))  
print(isArmstrong(0))     
