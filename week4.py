#Q1
#Password = 'Secret'
#Pass= input('Enter your password: ')
#if Password == Pass :
#    print('Access Granted')
#else :
#    print('Acess Denied')

#Q2
#ch= int(input('Enter number of credit hours earned '))

#if ch <= 30 and ch >= 0 :
#    print('You are a Freshman.')
#elif ch <= 60 and ch >= 31 :
#    print('You are a Sophomore.')
#elif ch <= 90 and ch >= 61 :
#    print('You are a Junior.')
#elif ch <= 122 and ch >= 91 :
#    print('You are a Senior.')
#else :
#    print("You entered an invalid number, please try again!") 

#Q3

from tkinter import Menu


hour = int(input('Enter the number of hours worked this week. ') )
hp = float(input('How much do you make per hour? '))
oh = float(hour - 40)

if hour > 40 :
    pay = float(40 * hp)
    opay = float(oh *(hp*1.5))
    tpay = opay + pay
    print('Your pay was $' + str(tpay))
else :
    pay = hour * hp
    print('Your pay was $' + str(pay))



#Q4

menu = ["Pizza", "Cheeseburger", "Taco", "Nothin"]
pizzap = 10
cheeseburgerp = 5
tacosp = 8

def func():
    order = int(input('1 for pizza, 2 Cheeseburger, 3 Taco, 4 for leave '))
    if order == 4:
        print('leave')
    elif order == 1:
        numpizza = int(input('How many would you like'))
        cost = numpizza * pizzap
        print('Your cost is $' + cost)
    elif order == 1:
        numburger = int(input('How many would you like'))
        cost = numburger * cheeseburgerp
        print('Your cost is $' + cost)
    elif order == 1:
        numtaco = int(input('How many would you like'))
        cost = numtaco * tacosp
        print('Your cost is $' + cost)
    else:
        print('Thank you')
    print('Fill out an online survey to win a free drink.')


