hour = int(input('Enter the number of hours worked this week. ') )
hp = float(input('How much do you make per hour? '))
oh = float(hour - 35)

if hour > 35 :
    pay = float(35 * hp)
    opay = float(oh *(hp*1.75))
    tpay = opay + pay
    print('Your pay was $' + str(tpay))
else :
    pay = hour * hp
    print('Your pay was $' + str(pay))


num = input('Enter a number ')
n = len(num) - 1
num1 = str(num[n])

print(num1)

if num1 == '2' :
    print('Your number is an even number')
else :
    if num1 == '4':
        print('Your number is an even number')
    else :
        if num1 == '6':
            print('Your number is an even number')
        else :
            if num1 == '8':
                print('Your number is an even number')
            else :
                if num1 == '0':
                    print('Your number is an even number')
                else : 
                    print('Your number is an odd number')


