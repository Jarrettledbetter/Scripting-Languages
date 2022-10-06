import numbers


for x in range (5, 10, 2):
    if x==7:
        continue
    print(x)

for x in range (3):
    for y in range (3):
        print(f'{x} , {y}')

for x in range (1, 30, 2):
    print(x)

for x in range (0, 21):
    print(x**2)

sum = 0 
numbers = [10,20,30,45,32]
for x in numbers :
    sum = sum + x
print ('Total price = ', sum)

cube_edge = [1, 5, 3, 10]
Sa = 0
for x in cube_edge:
    Sa = 6*x**2
    print(Sa)

adj= ['great', 'beautiful', 'awesome']
d= ['day', 'week', 'year']
for x in adj:
    for y in d:
        print (x,y)

for x in range (10, 0, -1):
    for y in range(x):
        print("*", end= " ")
    print(" ")


my_list= ['apple', 'banana', 'kiwi', 'apple', True, 1, 1.5]
print(my_list)
print(len(my_list))
print(type(my_list))
print(my_list[3])
print(my_list[2:5])
print(my_list[-5:-1])
my_list[1:4]= ['pineapple', 'lemon', 'melon']


colorlist = ['red', 'orange', 'yellow', 'green', 'blue']
print(colorlist[2])
print(colorlist[1:4])
print(colorlist[-3:-1])
colorlist[1] = "violet"
print(colorlist)
colorlist.append('brown')
print(colorlist)
colorlist.remove('yellow')