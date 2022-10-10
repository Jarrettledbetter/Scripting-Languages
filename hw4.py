for x in range (13 , 102, 2):
    print(x)

sumg = 0
counter = 0
gpa = 0
grades = [3.5,4.0,3.4,3.2,4,3.7]
while counter < 7: 
    for x in grades:
        sumg = sumg + x
        counter +=1
        if counter == 6:
            gpa = sumg / 6
            print(gpa)
    


