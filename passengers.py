from person import *

class Passenger(Person):
    def __init__(self, name,passport_number):
        super().__init__(name)
        self.passport_number = passport_number

    def add_passenger(self):
        self.name = input("Enter the passenger name: ")
        print(self.name)

    def add_passport_number(self,passport_number):
        self.passport_number = int(input("Enter the passport number: "))
        self.passport_number = passport_number

passenger_list = []
passenger1 = Passenger("Homer Simpson", 449374923424)
passenger2 = Passenger("Marge Simpson", 3939843424)
passenger3 = Passenger("Lisa Simpson", 1234839483)
passenger4 = Passenger("Bart Simpson", 3958393994)

passenger_list.append(passenger1)
passenger_list.append(passenger2)
passenger_list.append(passenger3)
passenger_list.append(passenger4)