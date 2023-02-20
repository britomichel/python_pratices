# operadores_logical_and_identity

# Logical Operators:
x = 5
print("x = ", x)
print("x > 3 and x < 10: ", (x > 3 and x < 10))
print("x < 5 or x < 4: ", (x < 5 or x < 4))
print("not(x < 5 and x < 10): ", (not(x < 5 and x < 10)))
print("- - - - - - - - - - - - - -")

# Bitwise Operators
print("6 & 3 (and) ? resp.: ", 6 & 3)
print("6 | 3 (or)? resp.: ", print(6 | 3))
print("6 ^ 3 (xor)? resp.: ", print(6 ^ 3))
print("~3 (not)? resp.: ", print(~3))
print("- - - - - - - - - - - - - -")

# Identity Operators:
arX = ["banana", "pêra", "maçã"]
arY = ["banana", "pêra", "maçã"]

print("arX: ", arX)
print("ary: ", arY)
print("arX == arY ? resp.: ", arX == arY)
print("arX is arY ? resp.: ", arX is arY)
print("arX is not arY ? resp.: ", arX is not arY)
