# Boolean
print(True)
print(False)

# Operators
# Integer
print('Addition: ', 1 + 1)
print('Subtraction: ', 1 - 1)
print('Multiplication: ', 2 * 3)
print('Division: ', 4 / 2)
print('Division: ', 5 / 2)  # Division in python gives floating number
print('Division without the remainder: ', 7 // 2)  # gives without the floating number or without the remaining
print('Modules: ', 3 % 2)  # Gives the remainder
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)  # it means 3 * 3

# Floating
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ', (1 + 1j) * (1 - 1j))

# Declaring and using and printing
a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Calculating area of a circle
radius = 10  # radius of a circle
area_of_circle = 3.14 * radius ** 2  # two * sign means exponent or power
print('Area of circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')  # Adding unit to the weight

# Calculate the density of a liquid
mass = 75  # in kg
volume = 0.075  # in cubic meter
density = mass / volume  # 1000 kg/m^3
print(density, 'kg/m^3')

# Comparison Operators
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in Asabeneh', 'A' in 'Asabeneh')
print('B in Asabeneh', 'B' in 'Asabeneh')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2', 4 is 2 ** 2)

# Logical Operators
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
print(3 < 2 and 4 < 3)
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3)
print('True or False: ', True or False)
print(not 3 > 2)
print(not True)
print(not False)
print(not not True)
print(not not False)
