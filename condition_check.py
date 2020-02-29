'''a = input('Enter a positive number: ')
a = int(a)
if a%2 == 0:
    print('Even number')
elif a%2 == 1:
    print('Odd number')

if a % 2 == 0:
    print('Even number')
else:
    print('Odd number')
'''

a = input('First Number: ')
a = int(a)
b = input('Second Number: ')
b = int(b)

'''if a>b:
    print(a)
else:
    print(b) '''

maximum = a
if b>a:
    maximum = b

print(maximum)
