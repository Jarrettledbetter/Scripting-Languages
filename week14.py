import random
fname= ['Rosie', 'John', 'Luke', 'Natalie', 'Kevin', 'Sophia', 'Bella']
lname= ['Carr', 'Jonson', 'Smith', 'White', 'Gray', 'Brown', 'Hart']
street= ['Jasmin', 'Spur', 'Black Walnut', 'Blue Ivy', 'Sunflower']
cityState= ['San Antonio, TX', 'Memphis, TN', 'St. Louis, MO', 'Atlanta, GA', 'Austin, TX', 'New York, NY'] 
for x in range (100):
    first = random.choice(fname)
    last = random.choice(lname)
    email = f'{first}.{last}@company.com'
    dataS = random.choice(street)
    StreetNo = random.randint(10, 99999)
    dataCS = random.choice(cityState)
    Zip = random.randint (10000, 99999)
    address = f'{StreetNo} {dataS}  \n{dataCS}, {Zip}'
    print(f'{first} {last}')
    print(email)
    print(address)
    print('**************************************************************')




while True:
    number = random.randint (1,10)
    choice = int(input('Enter a number between 1 and 10 '))
    if number == choice :
        print('You got it right')

    elif number > choice :
            print('You guessed too low')

    elif number < choice:
        print('You guessed too high')
        
    else:
        print('invaild input')
    exitchoice = input('Do you want to play again? (Y/N)')
    if exitchoice.lower() == 'n':
        break
    

while True : 
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input('Enter rock, paper, or scissors ')

    if computer_choice == user_choice:
        print(f'Both guesses were {user_choice}, it\'s a tie')

    elif computer_choice.lower() is 'rock' & user_choice.lower() is 'paper':
        print(f'You won!! You picked {user_choice} and the computer picked rock')
    
    elif computer_choice.lower() is 'scissors' & user_choice.lower() is 'rock':
        print(f'You won!! You picked {user_choice} and the computer picked scissors')

    elif computer_choice.lower() is 'paper' & user_choice.lower() is 'scissors':
        print(f'You won!! You picked {user_choice} and the computer picked paper')
    
    elif computer_choice.lower() is 'rock' & user_choice.lower() is 'scissors':
        print(f'You lost!! You picked {user_choice} and the computer picked rock')
    
    elif computer_choice.lower() is 'scissors' & user_choice.lower() is 'paper':
        print(f'You lost!! You picked {user_choice} and the computer picked scissors')
    
    elif computer_choice.lower() is 'paper' & user_choice.lower() is 'rock':
        print(f'You lost!! You picked {user_choice} and the computer picked paper')
    
    else: 
        print('invaild entry')


    echoice = input('Do you want to play again? (Y/N) ')
    if echoice.lower() == 'n':
        break
    







    

