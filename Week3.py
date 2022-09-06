# my_string= 'hello class!'
# print(my_string)

# print(my_string[0]) # prints index 0
# print(my_string[5]) # prints index 5
# print(my_string[2:9]) # prints from index 2 to index 9 but index 9 will not be printed
# print(my_string[:10]) # prints from the begining from the string to index 10
# print(my_string[3:]) # prints from index 3 to the end of the string

# print(len[my_string]) # prints the length of the string
# print(my_string[3:len(my_string)]) # prints from index 3 to the length of the string

# print('hello ' in my_string) # searches for certain phrase in string will print true
# print('Good moring ' in my_string) # will not print bc good moring is not in the string

##EXercises##

text= 'I love Python'
print(text[2:])

print('Python' in text)

if 'Python' in text:
    print('I found python in text!')

name = input('What is your name ')
lastname = input('What is your last name ')
print('Hello ' + name.capitalize() + ' ' + lastname.capitalize())

## Notes PT 2

# print(my_string.upper()) # returns the string in upper case
# print(my_string.lower()) # returns the string in lower case
# print(my_string.strip()) # removes any white spaces from the beginning or the end
# print(my_string.replace('h''j')) # replaces a string with another string
# print(my_string.capitalize()) # capitalize the first letter

# age= 25
# GPA= 3.6
# x= 'My name is Suzi and I am {} years old and my GPA is {}' # short cut to changing ints to fit a string
# print(x.format(age, GPA)) ^^
# print(f'My name is Suzi and I am {age} years old and my GPA is {GPA}') # easier way of formating int to fit a string

print('Hello\\world') # prints with a Backslash
print('It\'s a beatuifal day!') # prints with a Single Quote
print('This is \nCIS 2333 class') # prints on a New Line
print('This is\bCIS 2333 class') # prints with a Backspace