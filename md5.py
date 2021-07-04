#program to generate md5 of string data

import hashlib

print("Enter the string : ", end="")
str=input()

# encoding the input string using encode()
# then sending to md5()
result = hashlib.md5(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of md5 hash is : ", end="")
print(result.hexdigest())














