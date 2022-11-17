import week13p2 as mm
mm.personal_greeting('Jarrett', 'Ledbetter')

import math
print(dir(math))
print(math.ceil(12.5))
print(math.floor(12.5))
print(math.sqrt(64))

import mod11_user as Userr
#Userr.user2.describe_user()
Userr.user1.describe_user()

mylist= [1,2,3,4,5,6,7]
for x in mylist:
     print(f'The square root for {x} is ', math.sqrt(x))



userlist = []
for x in range(5) :
 userinput = int(input('Enter a number '))
 userlist.append(userinput)
print('The minimum value is ', min(userlist))
print('The maximum value is ', max(userlist))