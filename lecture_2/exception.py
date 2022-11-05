import sys
try:
    x=int(input("x= "))
    y=int(input("y= "))
except ValueError: #can not convert into int
    print("Invalid input.")
    sys.exit(1)

try:
  result = x/y
except ZeroDivisionError:
    print("Can not divide by 0.")
    sys.exit(1) #exit code 1 => something wents wrong

print(f"x/y = {result}")