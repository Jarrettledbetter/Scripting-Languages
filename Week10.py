mytuple= ('Sandy', 'Joe', 'Emma', 'Maddy')
for x in range(len (mytuple)):
    print(mytuple[x])
print(mytuple)

colors= ('blue', 'red', 'green', 'orange', 'pink', 'purple', 'red')
print(len(colors))
print(colors[1:3])
print(colors[-4:-2])
if 'red' in colors:
    print('Red is in the tuple red') 
x =colors.index('red')
print(x)
data = (1,2,3,4,5)
colorsdata= colors + data

myset= {'Sandy','Joe', 'Maria', 'Jorda'}
for x in myset:
    print(x)

A= {'Ford', 'Toyota', 'Doge', 'Nissan'}
B= {'Lexus', 'Ford', 'Audi'}

B.add('Honda')
print(B)
A.remove('Nissan')

C=A.union(B)
print(C)

print(A&B) # print (A.intersection(B))
print(A.difference(B))

print(A.symmetric_difference(B))

print(A ^ B)


#dict

data =  {'b':20, 'a':35}
data['b'] = -20
print(data)

data['c'] = 40
print(data)

data.pop('b')
print(data)

x= data.keys()
print(sorted(x))