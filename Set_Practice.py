num1 = {1,2,3,4,5,5,5}
num2 = set([4,5,6,7,8])

print(num1)
print(num2)

num1.add(7)
num2.add(2)

print(num1)
print(num2)

num1.remove(7)
num2.remove(2)

print(num1)
print(num2)

print(num1 & num2)
print(num1 | num2)
print(num1 - num2)


print(4 in num1)
print(4 not in num1)
print(6 in num1)
print(6 not in num1)
