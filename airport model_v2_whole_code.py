class Airport:

    def __init__(self):
        self.people = 0
        self.aircraft = True


class Aircraft():

    def __init__(self):
        super().__init__()
        self.flight_ready = True

        self.passenger_plane = True
        self.helicopter = True
        self.jet = True

class Plane():
    def __init__(self,plane_id):
        super(Plane, self).__init__()

        self.plane_id = plane_id


class Terminal():
    def __init__(self,terminal_number):
        super().__init__(terminal_number)
        self.terminal_number = ""
        self.terminal_location = ""

class Person():
    def __init__(self, name):
        self.name = name

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

class Flight:
    def __init__(self):
        self.plane = ""
        self.flight_route = ""
        self.flight_passengers_info = []
        self.destination = ""
        self.time = ""

    def add_passenger_to_list(self,passenger):

        self.flight_passengers_info.append(passenger)
        return(self.flight_passengers_info)

    def add_plane(self, plane):
        #add the plane to the flight info
        self.plane = plane
        return(self.plane)

    def add_flight_route(self,flight_route):
        self.flight_route = flight_route
        return(self.flight_route)

    def add_time(self,time):
        self.time=time
        return(self.time)

test_flight = Flight()
test_flight.add_plane('jkj')
print(test_flight.add_flight_route("London to Amsterdam"))

test_flight.add_passenger_to_list("Fred")
test_flight.add_passenger_to_list("Lucas")

# Adding passenger 1 - as an Object - Step by step
# Step 1 - Create a flight
# Step 2 - Create a Passenger object
passenger = Passenger("Lukus",1233)
# Save the passenger in a variable

# Step 3 - On the flight object, call the add_passenger_to_list method
print(test_flight.add_passenger_to_list(passenger))
# Step 3.2 - Send in the passenger object as the argument

# BOOM We have a list with on passenger object


# print(test_flight.add_plane("British Airways"))
# print(test_flight.add_plane, test_flight.add_passenger_to_list)





