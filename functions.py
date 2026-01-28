def factorial(number):
  
  if number < 0:
    return "Factorial is not defined for negative numbers"
  elif number == 0:
    return 1
  else:
    factorial_result = 1
    for i in range(1, number + 1):
      factorial_result *= i
    return factorial_result


a=int(input("Enter a number"))
print(f"The factorial of {a} is {factorial(a)}")


import math


num = float(input("Enter a number: "))


square_root = math.sqrt(num)
natural_log = math.log(num)     
sine_value = math.sin(num)       


print("Square root:", square_root)
print("logarithm ", natural_log)
print("Sine ", sine_value)

