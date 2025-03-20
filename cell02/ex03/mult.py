#!/usr/bin/env python3

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
result = (num1 * num2)
if result>0 :
    print("The result is positive ")
elif result<0 :
    print("The result is negative ")
else :
    print("The result is positive and negative ")
print(f"{num1} * {num2} = {result}")
