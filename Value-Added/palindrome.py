
def isPalindrome(n: int) -> bool:
    original = n
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    
    return original == rev

# Example runs
print(isPalindrome(121))   
print(isPalindrome(123))   
print(isPalindrome(0))     
print(isPalindrome(1221))  
