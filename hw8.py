class Patient :
    def __init__ (self, First_name, last_name, phone_number, age) :
        self.First_name = First_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age

    def Patient_Info(self):
        print(f'{self.First_name} {self.last_name}\'s phone number is {self.phone_number} and age is {self.age}')

Patient1 = Patient('Jarrett', 'Ledbetter', '2921919002', '20 ')

class Kid(Patient):
    def __init__ (self, First_name, last_name, phone_number, age , IsImmunization) :
        super().__init__(First_name, last_name, phone_number, age)
        self.IsImmunization = IsImmunization


    def Display_Immunization_Info(self) :
        print(f'{self.First_name} is up to date' , bool(self.IsImmunization))


Kid1 = Kid('Gingerbread', 'Man', '2351679002', '10 ', 'True')

print(Patient1.First_name)
print(Patient1.last_name)
Patient1.Patient_Info()
Kid1.Patient_Info()
Kid1.Display_Immunization_Info()