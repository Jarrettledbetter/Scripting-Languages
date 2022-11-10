class Resturant:
    def __init__(self, res_name, Q_type, number_served = 0):
        self.res_name= res_name
        self.Q_type= Q_type
        self.number_served = number_served
  
    
    def describe_resturant(self):
        print(f'{self.res_name} is a/an {self.Q_type} resturant')

    def open_resturant(self):
        print('Welcome the resturant is open!')
    
    def set_number_served(self, new_numServed):
        self.number_served = new_numServed
        return self.number_served


    def increment_of_number_served(self,inc):
        self.number_served+= inc
        return self.number_served
    
resturant1 = Resturant('Little Italy', 'Italian')

print(resturant1.res_name)
print(resturant1.Q_type)

print(resturant1.number_served)
resturant1.number_served = 140
print(resturant1.number_served)

resturant1.describe_resturant()
resturant1.open_resturant()

res2 = Resturant('BK', 'Fast Food')
res3 = Resturant('The Branch Grill', 'American')
res2.describe_resturant()


res2.set_number_served(500)
print(res2.number_served)
res2.increment_of_number_served(300)
print(res2.number_served)


class user:
    def __init__(self, first_name, last_name, membership, day_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership
        self.day_joined = day_joined

    def describe_user(self):
        print('This account has been active since ' + self.day_joined )
        print('Your memebership status is ' + self.membership)

    def greet_user(self):
        print('Welcome back ' + self.first_name)

user1 = user('Jarrett', 'Ledbetter', 'Gold', 'August 26')
user1.describe_user()
user1.greet_user()
