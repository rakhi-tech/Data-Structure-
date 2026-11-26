class InvalidAgeError(Exception):
    pass
try:
    age=15
    if age < 18:
        raise InvalidAgeError("you are under age")
#except InvalidAgeError as i:
    #print("error",i)
finally:
    print("program completed")

