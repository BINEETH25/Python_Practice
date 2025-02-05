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


-------------------------------------------------------'''
'''
# 16. Function and Return.
# parameter and argument

#4 types of arguments : positional, default, keyword, arbitrary(*args --> tuple, **kwars --> dictionary).


def add(*args):
	total = 0
	for arg in args:
		total += arg
	return total

print(add(1,2,3,4))

-------------------------------------------------------'''
'''
# 17. Iterables, # 18. Membership operators(in, not in)

# 19.List Comprehension: [expression for value in iterable if condition]
# --> A Concise way to create lists, compact and easier to read than traditional loops

numbers = [1, -2, 3, -4, 5, -6]
# lets make a list of positive numbers

pos_nums = [num for num in numbers if num >= 0]
print(pos_nums)

# 20. Match- Case Statement(Switch ) py 3.10 or above

def is_weekend(day):
	match day:
		case 'Saturday' | 'Sunday':
			return True
		case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
			return False
		case _:
			return 'Not a Valid day'

print(is_weekend('Sunday'))

-------------------------------------------------------'''
# 21. Modules : A files containing a code, we want to use
#print(help('modules'))
#print(help('math'))

# 22. Variable scope : Where a variable is visible and accesible
# scope resolution : (LEGB)  Local -> enclosed -> Gloabal -> Built-in

# 23. Main Function : if __name__ = __main__: main()


'''-------------------------------------------------------'''
'''
# Exercise : A Banking Program

def show_balance(balance):
	print('******************************')
	print(f'Your balance is {balance:.2f}')
	print('******************************')

def deposit():
	amount = float(input('Enter amount to deposit: '))
	if amount < 0:
		print('******************************')
		print('Enter Valid Amount')
		print('******************************')
		return 0
	else:
		return amount
	

def withdraw(balance):
	print('******************************')
	amount = float(input('Enter Amount to Withdraw: '))
	print('******************************')
	if amount < 0:
		print('******************************')
		print('Enter Valid Amount')
		print('******************************')
		return 0
	elif amount > balance:
		print('******************************')
		print('Insufficient funds')
		print('******************************')
		return 0
	else:
		return amount

def main():

	balance = 0

	is_running = True

	while is_running:
		print('******************************')
		print('Banking Program')
		print('******************************')

		print('1. show_balance')

		print('2. deposit')

		print('3. withdraw')

		print('4. exit')
		print('******************************')
		choice = input('Enter a choice (1 - 4): ')
		print('******************************')

		if choice == '1':
			show_balance(balance)
		elif choice == '2':
			balance += deposit()
		elif choice == '3':
			balance -= withdraw(balance)
		elif choice == '4':
			is_running = False 
		else:
			print('******************************')
			print('Invalid choice')
			print('******************************')
	print('******************************')
	print('Thank You, Have a Nice day..!')
	print('******************************')

if __name__ == '__main__':
	main()

-------------------------------------------------------'''
'''
# Exercise : Substitution Cipher Program 

# String values
import random
import string

#w = string.whitespace
#s = string.punctuation
#d = string.digits
#l = string.ascii_letters

#print(w)
#print(s)
#print(d)
#print(l)

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy() # copying chars list

random.shuffle(key) # shuffling items in list Key

#print(f'Chars :{chars}')
#print(f'Key   : {key}')

plain_text = input('Enter a Message to Encrypt: ')
cipher_text = '' #message to encrypt

for letter in plain_text:
	index = chars.index(letter)
	cipher_text += key[index]

print(f'Original Message  : {plain_text}')
print(f'Encrypted Message : {cipher_text}')

cipher_text = input('Enter a Message to Decrypt: ')
plain_text = ''

for letter in cipher_text:
	index = key.index(letter)
	plain_text += chars[index]

print(f'Encrypted Message :{cipher_text}')
print(f'Decrypted Message : {plain_text}')
-------------------------------------------------------'''

''' 572
# Exercise : Hangman Game Program

# lets make a dictionary art of hangman
# include 2 \\ 

import random

words = ('apple', 'orange', 'kiwi', 'lemon', 'sapota')

hangman_art = {	0:(	'   ',
					' 	',
					'   '),
				1:( ' o ',
					' 	',
					'   '),
				2:( ' o ',
					' |	',
					'   '),
				3:( ' o ',
					'/| '
					'   '),
				4:( ' o ',
					'/|\\',
					'   '),
				5:( ' o ',
					'/|\\',
					'/  '),
				6:( ' o ',
					'/|\\',
					'/ \\')}

#for index in hangman_art[6]:
#	print(index)

def display_man(wrong_guesses):
	print('**************')
	for line in hangman_art[wrong_guesses]:
		print(line)
	print('**************')

def display_hint(hint):
	print(' '.join(hint))

def display_answer(answer):
	print(' '.join(answer))

def main():
	answer = random.choice(words)
	#print(answer)
	hint = ['_'] * len(answer)
	#print(hint)
	wrong_guesses = 0
	guessed_letters = set()
	is_running = True

	while is_running:
		display_man(wrong_guesses)
		display_hint(hint)
		guess = input('Enter a Letter: ').lower()
		
		if len(guess) != 1 or not guess.isalpha():
			print('Invalid input')
			continue

		if guess in guessed_letters:
			print(f'{guess} is already guessed')
			continue

		guessed_letters.add(guess)

		if guess in answer:
			for i in range(len(answer)):
				if answer[i] == guess:
					hint[i] = guess
		else:
			wrong_guesses += 1

		#display_answer(answer)
		if '_' not in hint:
			display_man(wrong_guesses)
			display_answer(answer)
			print('You Win..!')
			is_running = False
		elif wrong_guesses >= len(hangman_art) - 1:
			display_man(wrong_guesses)
			display_answer(answer)
			print('You Lose')
			is_running = False


if __name__ == '__main__':
	main()


477------------------------------------------------------'''



'''------------------------------------------------------'''

		# 24.Object Oriented Programming

'''------------------------------------------------------'''

'''--#641
# Object : A 'bundle' of related attributes(parameters) and methods(functions)
# Class : (Blueprint) Used to design the structure and layout of the object

# Method is a function that belongs to an object

# In a class, to create object we need constructor(Special type of method)

# . --> attribute access operator

# self --> to assign the attibutes we access self

class Car:
	def __init__(self, model, year, color, for_sale):
		self.model = model
		self.year = year
		self.color = color
		self.for_sale = for_sale

car1 = Car('Mustang', 2025, 'Blue', False)

print(car1.year)

# 25. Inheritance : Allows a class to inherit attributes and methods from another class
	# class Sub(Super)

	# multiple Inheritance : C(A, B)
	# multi-level Inheritance : C(B) <- B(A) <- A

	# super() : Function used in a child to call methods from a parent class(Super class)


class Shape():
	def __init__(self, color, is_filled):
		self.color = color
		self.is_filled = is_filled

class Circle(Shape):
	def __init__(self, color, is_filled, radius):
		super().__init__(color, is_filled)
		self.radius = radius

class Square(Shape):
	def __init__(self, color, is_filled, width):
		super().__init__(color, is_filled)
		self.width = width

class Triangle(Shape):
	def __init__(self, color, is_filled, heigth, width):
		super().__init__(color, is_filled)
		self.heigth = heigth
		self.width = width

circle = Circle(color = 'Blue', is_filled = True, radius = 5)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

--583----Class, Inheritance, super()--------------------------------------------------------------  '''

# 26. Polymorphism : can be achieved by (1. Inheritance, 2. Duck Typing)

# 27. Static Methods: A Method that belongs to a class rather than any objects in that class
# --> only needs to access the class directly, don't have to create any objects in that class
# Instance Method : First we have to access an object.


class Employee:

	def __init__(self, name, position):
		self.name = name
		self.position = position

	def get_info(self):

		return f'{self.name} = {self.position}' # membership operator


	@staticmethod
	def is_vaild_position(position):
		valid_positions = ['Manager', 'Cook', 'Cashier', 'Janitor']
		return position in valid_positions

print(Employee.is_vaild_position('Cashier'))

employee1 = Employee('Binny','Student')

print(employee1.get_info())







