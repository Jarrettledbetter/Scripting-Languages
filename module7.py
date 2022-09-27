counter = 0
while counter<11:
    print(counter)
    if counter == 5:
        break
    counter+=1
print('I\'m done counting!')


counter = 0
while counter<11:
    print(counter)
    counter+=2
print('I\'m done counting!')

count = 0
num = input('Enter a number: ')
while count < 10 :
    print(count + int(num))
    count+=1
print("Finished")

num = input('Enter a postitive number: ')
fac = 1
if num <= 1:
        print(fac)
elif num>1:
    while num>1:
        fac=fac*num
        num-=1
    print(fac)
print('Finished')

