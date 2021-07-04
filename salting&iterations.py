#salting to hashes
import hashlib
import uuid

print("Enter the string : ", end="")
str=input()
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512((str+salt).encode()).hexdigest()
print("The hexadecimal equivalent of hash with salt is : ", end="")
print(hashed_password)
print("\r")

#iteration
iteration=100
# using the salted hash for iterations
for i in range(iteration):
    hashed_password = hashlib.sha512(hashed_password.encode()).hexdigest()
print("The hexadecimal equivalent of salted hash after {} iteration is : " . format(iteration), end="")
print(hashed_password)
