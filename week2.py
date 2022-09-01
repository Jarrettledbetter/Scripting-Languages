
x = 1 #int
y = 2.8 #float
z = 1j #complex

grocey_list = ['apple', 'banana', 'grapes', 'pineapple'] #list 

days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') #tuple

Dictionary = {'Dog', 'Cat', 'turtle'} #Dictionary

# numbers in input must be made into a string
age = 20

print('My age is '+str(age)+ 'years old')

# int stored as strings must be made into a int or float and float will add a decimal
num1 = input('Enter a number')
num2 = input('Enter a number')
total= float(num1) + float(num2) 
print(total)

# boolean statements return true or false
a = 55
b = 21
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#examples of booleans
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))