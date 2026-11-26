age = 15
try:
 if age < 18:
    raise ValueError("you are under age")
except ValueError as e:
 print("error",e)
else:
 print("access granted")