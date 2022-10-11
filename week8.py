scores = [100, 200, 300, 400, 500, 1000]

choice = 1

while choice>0 :
    print('0 -- Exit')
    print('1 -- Show Scores')
    print('2 -- Add a Score')
    print('3 -- Remove a Score')
    print('4 -- Sort Scores')
    choice = int(input('Choice : '))

    if choice == 1:
        print(scores)
    elif choice == 2:
        x = int(input('Enter a new score '))
        scores.append(x)
    elif choice == 3:
        print(scores)
        x = int(input('Enter the score you wish to remove '))
        scores.remove(x)
    elif choice == 4:
        sortc = input('Do you want to sort in reverse (Y/N) ')
        if sortc == 'Y':
            scores.sort(reverse=True)
        else:
            scores.sort

