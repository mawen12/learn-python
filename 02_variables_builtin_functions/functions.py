print('Hello World!')
len('Hello World!')
type('Hello World!')
str(10)
int('10')
float(10)
print(input('Enter your name:'))
help('keywords')  # prints all python reserved words
help(str)
dir(str) # give information about string

min(20, 30, 40, 50)  # gives the minimum value
max(20, 30, 40, 50)  # gives the maximum value
min([20, 30, 40, 50])  # it takes list as an argument and return min
max([20, 30, 40, 50])  # it takes list as an argument and return max
sum([20, 30, 40, 50])  # it takes only list as an argument and return the sum

# Data type Casting
# int to float
num_int = 10
print('num_int:', num_int)
num_float = float(num_int)
print('num_float:', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_str = '10.6'
# print('num_int:', int(num_str)) # it will throw error
print('num_float:', float(num_str))

# str to list
first_name = 'Aasbeneh'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list) # ['A', 'a', 's', 'b', 'e', 'n', 'e', 'h']
