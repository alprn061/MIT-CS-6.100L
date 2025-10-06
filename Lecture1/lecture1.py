## SCALAR OBJECTS

# int
a = 5
#float
b = 3.0
#bool
c = False
#NoneType
d = None


print(type(a))
print(type(b))
print(type(c))
print(type(d))


# When an object is cast to a different type, the existing object is not changed, a new object is created
print(f"Converting from float to int: {int(3.9)}")


## EXPRESSIONS

#* python reads the expressions from left to right and follows the order of operations and does not store the expression but the result of the expression
# <object> <operator> <object> <operator> <object>
x = a + b *2   # (x = a + b *2) is statement, (a + b *2) is expression


## OPERATORS ON int and float
print(f" if both values are int, the result is int: {2+2, 2*2, 2-1} \n if one value is float, the result is float: {2.0+2, 2*2.0, 2-1.0} \n Division always returns float: {3/2, 4/2}")
print(f"Floor division (//) returns the largest integer less than or equal to the division result: {3//2, 4//2, 5//2, 6//2} ")
print(f"if one value is float, the result is float, otherwise int: \n Modulus (%) returns the remainder: {3%2, 4%2, 5%2.0} \n Exponentiation (**) raises the number to the power of the exponent: {2**3, 3**2.0}")