'''
A.Basic Syntax & Data Types

	1.Write a program to swap two numbers without using a third variable.
	
	2.Given a string, reverse it without using built-in functions.
	
	3.Write a program that checks if a number is even or odd.
	
	4.Create a program that takes user input and converts it to an integer, float, and string.
'''
'''
# A.1

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

a = a + b
b = a - b
a = a - b

print(a,b)
	
'''
'''
# A.2

a = input('Enter a String: ')
rev = ""
for i in a:
	rev = i + rev
print(rev)
'''
'''
# A.3

n = int(input('Enter a Number: '))

if n % 2 == 0:
	print('Even')
else:
	print('Odd')
'''
''' # cannot handle exceptions here
# A.4

n = input('Enter input: ')

i = int(n)
print(type(i))
f = float(n)
print(type(f))
s = str(n)
print(type(s))
'''
'''
B. Control Flow (if-else, loops)

	5.Write a program to find the largest of three numbers.
	
	6.Print all prime numbers from 1 to 100.
	
	7.Print the Fibonacci series up to N terms (N is user input).
	
	8.Count the number of vowels and consonants in a given string.

'''
'''
# B.5
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))

if a >= b and a >= c:
	print('a is largest ', a)
elif b >= a and b >= c:
	print('b is largest ', b)
else:
	print('c is largest ', c)
'''

for i in range(3, 101):
	if (i % (i/2 - 1)) == :
		print(i)









































