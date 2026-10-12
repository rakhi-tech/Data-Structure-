
def largestDigit(n: int) -> int:
    largest = 0
    while n > 0:
        digit = n % 10       
        if digit > largest:  
            largest = digit
        n //= 10             
    return largest

# Example runs
print(largestDigit(25))    
print(largestDigit(123))   
print(largestDigit(987))   
print(largestDigit(0))     
