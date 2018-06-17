#!bin/python3

print("Hello!")

print('Here\'s a picture of a dog:')
print("  o____  ")
print("   ||||  ")

print('''
Here's a cow face:

    ^  ^
    (oo)
    (  ) 
''')

born = int(input('What year were you born?: '))
age = 2025 - born
print("In the year 2025 you'll be", age ,"years old." )

# challege - dog age
age = int(input('What is your age?:'))
dog_age = age * 7
print("If you were a dog, you'd be", dog_age,"!!")
print('''
o____
 ||||
''')

# Calculating text
print('ha ' *4)
print('ba' + 'na' *2)
print('Hello' + '!' *10)