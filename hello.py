
'''
print('Hello..!')
x = 11%2
print(x)
name = input('Who are you? ')
print('hi ', name)

eun = input('which floor? ')
usf = int(eun) + 1
print('usf:', usf)
'''
'''
print('hi', '12')
x = int(98.6)
print(x)
'''
'''
hrs = input("Enter hours:")
print(type(hrs))
rate = input("Enter Rate:")
print(type(rate))
# A floating input, can be taken input as string and type conversion to int causes valueError.
rate = float(rate)
print(type(rate), rate)
'''

'''
hrs = input("Enter hours:")
rate = input("Enter Rate:")
try: 
	h = float(hrs)
	r = float(rate)
except:
	print("Error input, please enter numberic input")
	quit()

'''
'''
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
'''
'''

def computepay(h,r):
	if h <= 40:
		pay = h * r
		return pay
	else:
		dif = h - 40
		er = 1.5 * r
		tpay = dif * er + 40 * r
		return tpay

h = float(input("Enter hours:"))
r = float(input("Enter rate:"))
p = computepay(h,r)
print(p)

'''

'''
num = 0
tot = 0

while True:
	sval = input("Enter a Number:")
	if sval == 'done':
		break
	try:
		fval = float(sval)
	except:
		print('Invalid input')
		continue
	#print(fval)
	num = num + 1
	tot = tot + fval
print(tot, num, tot/num)
'''
'''
smallest = None
largest = None

while True:
	num = input('Enter a Number: ')
	if num == 'done':
		break
	try:
		num = int(num)
	except:
		print('Invalid input')
		continue

	if largest is None or num > largest:
		largest = num

	if smallest is None or smallest > num:
		smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)

'''
'''
fruit = 'banana'
index = 0 

while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

'''
'''
fruit = 'banana'
count = 0

for letter in fruit:
	print(letter)
	if letter == 'a':
		count = count + 1
print(count)

'''
'''
stri = 'Hello'
print(type(stri))
print(dir(stri))

'''
'''
print(len('banana')*7)
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
'''
'''
text = "X-DSPAM-Confidence:    0.8475"

t1 = text.find('0')
num = float(text[t1 : ])
print(num)

'''
'''
fhand = open('test.txt')
count = 0

for line in fhand:
	line = line.rstrip()
	count = count + 1
	if line.startswith('From: '):
		print(line)
print('Line count: ', count)

'''
'''
filename = input('Enter filepath: ')
fhand = open(filename)
for line in fhand:
	txt = line.rstrip()
	print(txt.upper())
'''
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ext = line.rstrip()
    num = ext[20:]
    n = num.strip()
    n1 = float(n)
    count = count + 1
    total = total + n1
print("Average spam confidence:", total/count)
'''
''' #8.4 printing words in list by removing duplicates
file = open('romeo.txt')
words = list()
sep = list()
for line in file:
	#print(line.rstrip())
	lst = line.split()
	# print(lst)
	words = words + lst
#print(words)

for word in words:
	if word in sep:
		continue
	sep.append(word)
	sep.sort()
print(sep)
'''

'''# 8.5

mail = open('mbox-short1.txt')
lis = list()
count = 0
for line in mail:
	if line.startswith('From '):
		count = count + 1
		lis = line.split()
		#lis.append(line)
		#print(line)
		#print(lis)
		#lis[1] = ('[email protected]')
		#name = lis[1].rstrip()
		print(lis[1])
#print(type(line))
print("There were", count, "lines in the file with From as the first word")

'''
'''
oo = { }
print(type(oo))
'''
'''
# dictionary, counting most common word

file = open('romeo.txt')
lis = list()
counts = dict()

for line in file:
	words = line.split()
	lis = lis + words

for word in lis:
	counts[word] = counts.get(word, 0) + 1

for key in counts:
	print(key, counts[key])

bigword = None
bigcount = None

for key,value in counts.items():
	if bigcount is None or value > bigcount:
		bigcount = value
		bigword = key

print('bigword: ', bigword , 'bigcount: ',bigcount)

print('Counts:', counts)
'''

''' # number of mails from single name
file = open('mbox-short.txt')
counts = dict()
for line in file:
	if line.startswith('From '):
		#print(line)
		words = line.split()
		counts[words[1]] = counts.get(words[1], 0) + 1

bigcount = None
bigword = None

for key, value in counts.items():
	if bigcount is None or value > bigcount:
		bigcount = value
		bigword = key

print(bigword, bigcount)

'''


file = open('mbox-short.txt')
counts = dict()
val = list()
for line in file:
	if line.startswith('From '):
		words = line.split()
		x = words[5]
		val.append(x[:2])

#print(val)
for key in val:
	counts[key] = counts.get(key, 0) + 1
#print(counts)
#print(sorted([(key,v) for (key,v) in counts.items()]))
for k,v in sorted(counts.items()):
	print(k,v)










