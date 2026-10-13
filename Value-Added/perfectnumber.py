#perfect number
def isperfectnumber(n):
 if n<=1:
  return False
 divisor = 1
 for i in range(1,n):
  if n%i==0:
   divisor+=i
  return divisor == n
  