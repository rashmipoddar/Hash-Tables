import hashlib

n = 10
key = b"string"
key2 = "string".encode()
key3 = "string1".encode()
key4 = b"lunchtime"

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
index4 = hash(key4) % 8

print(index)
print(index2)
print(index3)
print(index4)

# The built in hash of python gives a different value with the same input every time it is run
# We are using sha256 to get a consistent output

for i in range(n):
  print(hash(key))
  print(hashlib.sha256(key).hexdigest())

# for i in range(n):
#   print(hash(key))

# for i in range(n):
#   print(hash(key2))