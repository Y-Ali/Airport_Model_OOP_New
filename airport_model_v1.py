class Airport():
    
    def __init__(self):
        self.people = 0
        self.aircraft = True

class Aircraft():

    def __init__(self):
        super().__init__()

        self.passenger_plane = True
        self.helicopter = True
        self.jet = True

class People():
    def __init__(self):
        super().__init__()
        self.passengers = 0
        self.staff = 0
        self.passenger_names = []
        self.passport_number = []
        #print(self.passport_number)

class Terminal():
    def __init__(self):
        super().__init__()
        self.terminal_number = 0

class Flight(People):
    def __init__(self):
        super().__init__()
        self.flight_route = [""]
        self.flight_passengers_info = []
        self.destination = [""]



add_info = People()                                                     # create attribute for class People
print("Passport number type: ",type(add_info.passport_number))          # test to see if this is a list
add_info.passport_number.append(123456)                                 # add a passport number to the list
print("added passport number: ", add_info.passport_number)              # check if appending was successful
add_info.passenger_names.append("Yousuf")                               # add a passenger to the passenger_names list
print(add_info.passenger_names)                                         # check if passenger has been added

flight_info = Flight()                                                  # create attribute for class Flight
flight_info.flight_passengers_info.append(add_info.passenger_names)     # add passenger name from class People to-
                                                                        #   flight_passengers_info in class Flight
print("added passenger to flight: ",flight_info.flight_passengers_info)
flight_info.flight_passengers_info.append(add_info.passport_number)     # add passenger passport number from class People to-
                                                                        #   flight_passengers_info in class Flight.
print("Flight info for 1 passenger: ", flight_info.flight_passengers_info)


