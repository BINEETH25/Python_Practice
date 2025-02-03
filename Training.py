# This is for single line comment
'''
# f- string : formatted string literal (python 3.6 > ) 

before f-string : we can use %() or after python2.7 >  we used .format()
'''
'''
# 1.variables :  'string', integer, float, boolean

name = 'Binny'
age = 25

print(f'This is {name} and i am {age}')

# 2.TypeCasting :  converting a variable of one data type to another 
# type()
# str(), int(), float(), bool()

x = bool(age)
print(x)

# 3.User input : input() --> prompts the user to enter data 
# --> returns the entered data in string

name = input('Enter a Name ')
age = int(input('Enter age: '))
 # we type cast here because user entered data will be returns in string 
age += 1
print(f'user {name} is {age} years old')

------->  1 to 3'''
'''
# Exercise 1 : Calucation of Rectangle area by using lenght and width from user

length = float(input('Enter length: '))
width = float(input('Enter width: '))

Area = length * width

print(f'Area of Rectangle {Area} cms')

# Exercise 2 : Shopping Cart Program

item = input('item name: ')
price = float(input('Price of item: '))
quantity = int(input('How many: '))

total = price * quantity

print(f'Total Price of {quantity} {item} : {total}')

'''
# 4. Arithmetic Operations, Augumented Assignments
# +=, -=, *=, /=, **= , %=
# round(), abs() -->prints value how much farther from zero, 
# pow(x, y) --> prints x power y value
# max(), min() --> prints max or min value : if more than 1 variables passed

'''
#5. math constants --> .pi, .e, .sqrt(), .ceil(), .floor()
import math
print(math.pi)
print(math.e)
x = 9

print(math.sqrt(x))

# Exercise 3:  Circumference of a Circle 

r = float(input('Enter Radius: '))
cir = 2 * math.pi * r
# Using round() to truncate extra decimal values
print(f'circumference of circle {round(cir,2)}cm with radius {r}')

Area = math.pi * pow(r, 2)
print(f'Area of circle {round(Area,2)}')

import math

a = float(input('a: '))
b = float(input('b: '))
#c = pow(a, 2) + pow(b, 2)
hyp = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Hypotheis of right angle triangle is : {round(hyp, 2)}')

'''

# 6. if - statements , if, elif, else : if one statement is true it won't execute next statements

'''
# 7. Sample Calculator

operator = input('Enter a operator (+, -, /, *): ')
a = float(input('Enter a number: '))
b = float(input('Enter a number: '))

if operator == '+':
	print(a + b)
elif operator == '-':
	print(a-b)
elif operator == '/':
	print(a/b)
elif operator == '*':
	print(a*b)
else:
	print(f'{operator} is not valid')

'''
'''
# 8. Weight converter

weight = float(input('Enter weight: '))
unit = input('Enter (k, l): ')

if unit == 'k':
	weight = weight * 2.205
	unit = 'lbs'
	print(f'Your weight {round(weight, 1)} {unit}')
elif unit == 'l':
	weight = weight / 2.205
	unit = 'kgs'
	print(f'Your weight {round(weight, 1)} {unit}')
else:
	print(f'{unit} is not valid')

'''
'''
# 9. Temperature Conversion

unit = input('Enter (C, F): ')
temp = float(input('Enter temp: '))

if unit == 'C':
	temp = round((temp * 9 )/5 + 32, 1)
	unit = 'F'
	print(f' temp {temp} {unit}')
elif unit == 'F':
	temp = round((temp - 32) * 5/9, 1) 
	unit = 'C'
	print(f' temp {temp} {unit}')
else:
	print(f'{unit} is not valid')
'''

# 10. Logical Operators : (or, and, not)
# 11. Conditional Expression : X if condition else Y
'''
x = -5
print("Positive" if x > 0 else "Negative")
'''
'''
# 11.string Methods : help(str), .capitilize(),
# .len(str), .find(), .rfind(), .upper(), .lower(), 
# .isdigit(), .isalpha(), .replace('old', 'new')

username = input('Enter Username: ')
x = len(username)
print(x)

if x < 12 and username.isalpha() and not username.isdigit():
	print(username)
else:
	print(f'Invalid Username')

'''

# 12. String Indexing : [Start : end : Step]

# to reverse a string, we can use [::-1] or last 4 digits [-4:]

# 13. format specifiers : (:2f, :+, ...)

'''
# Exercise 4. Timer and Count-down Timer program

import time

my_time = int(input('Enter timer in seconds: '))
# Instead of use of reversed, i used :  range(last , start , step: -1)
for i in range(my_time, 0, -1):
	seconds = i % 60
	minutes = int(i / 60) % 60
	hours = int(i / 3600) 
	print(f'{hours:02}:{minutes:02}:{seconds:02}')
	time.sleep(1)
print('Times Up')

'''
'''
# 14. Nested Loop : A loop in another loop

rows = int(input('Enter Rows: '))
cols = int(input('Enter Cols: '))
sym = input('Enter a Symbol: ')

for i in range(rows):
	for j in range(cols):
		print(sym, end=' ')
	print() # for new line
'''

# 15. Collections : A variable can contain more than one value
# list --> ordered and changeable, duplicates allowed
# set --> unordered and unchangeable, no duplicates allowed
# tuple --> ordered and unchangeable, duplicates allowed

# 2D Collection, phonepad --> tuple of tuple
'''
phone_pad = (
	(1, 2, 3),
	(4, 5, 6),
	(7, 8, 9),
	('*', 0, '#'))

for row in phone_pad:
	for val in row:
		print(val, end= ' ')
	print()

'''
''' --------------------------------------------------
# Python : Quiz Game

questions = ('how many cards in a deck?',
	'how many cards in a set?',
'how many colors in rainbow?'
,'how many bones in human body?'
,'how many hours per day?')

options = (
	('A. 50', 'B. 52', 'C. 54','D. 56'),
	('A. 12', 'B. 13', 'C. 14','D. 15'),
	('A. 6', 'B. 7', 'C. 8','D. 10'),
	('A. 203', 'B. 204', 'C. 206','D. 208'),
	('A. 20', 'B. 21', 'C. 24','D. 22'))

answers = ['B', 'B', 'B', 'C','C']

guesses = []
question_num = 0
score = 0

for question in questions:
	print(question)
	for option in options[question_num]:
		print(option)
	print('-------------------------------')

	guess = input('Enter Your guess (A, B, C, D): ').upper()
	guesses.append(guess)
	if guess == answers[question_num]:
		score += 1
		print('Correct Answer')
	else:
		print('Incorrect Answer')
		print(f'{answers[question_num]} is Correct Answer')

	question_num += 1

print('------------------------------')
print('            RESULTS           ')
print('------------------------------')

print('answers', end=' ')
for answer in answers:
	print(answer, end = ' ')
print()

print('guesses', end=' ')
for guess in guesses:
	print(guess, end=' ')
print()

total = score/question_num * 100

print(f'Final Score : {total}%')

------------------------------------------------------'''
'''
# 15. Random
import random

low = 1
high = 100
options = ('abc', 'bcd', 'cde', 'efg')
cards = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q','K','A']
#num = random.randint(low, high)
#print(num)
#floa = random.random()
#print(floa)
#st = random.choice(options)
#print(st)
random.shuffle(cards)
print(cards)
'''



















