n = int(input("enter the number"))
rev=0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    
    n//=10
    if n == rev:
        print("It is a palindrome")
    else:
        print("it is not a palindrome")

