from person import *
from passengers import *
from flight import *

#test_flight = Flight(plane,flight_route, destination, time)
# test_flight.add_plane('jkj')
# print(test_flight.add_flight_route("London to Amsterdam"))
#
# test_flight.add_passenger_to_list("Fred")
# test_flight.add_passenger_to_list("Lucas")

# Adding passenger 1 - as an Object - Step by step
# Step 1 - Create a flight
# Step 2 - Create a Passenger object
# passenger = Passenger("Lukus",1233)
# Save the passenger in a variable

# Step 3 - On the flight object, call the add_passenger_to_list method
# print(test_flight.add_passenger_to_list(passenger))

# Step 3.2 - Send in the passenger object as the argument

# BOOM! We have a list with on passenger object

#print(type(passenger_list[0]))

# for passenger in passenger_list:
#     print("Passenger Name: ",passenger.name," " ,"Passport Number: ",passenger.passport_number)

# print("\n")
# for flight in flights_list:
#     print(f"{flight.plane}, {flight.flight_route}, {flight.destination}, {flight.time}")
#
# print(flights_list[0].destination)
while True:
    count = 0
    #test_flight = Flight()
    #print(type(flight1))
    user_input = int(input("\nPlease select an option from the following:\n 1. Create a passenger\n 2."
                           " List the flights\n 3. Add passenger to existing flight\n 4. See Details of a flight : >"))
    if user_input == 1:
        print("You selected: 1. Create a passenger\n")
        name = input("What's the passenger name?: ")
        passport_num = input("What is the passengers passport number?: ?")
        print(f"You created a passenger {name}, {passport_num}")

        new_passenger = Passenger(name, passport_num)
        #print(type(new_passenger))

        passenger_list.append(new_passenger)
        print("\n")
        for passenger in passenger_list:
            print("Passenger Name: ", passenger.name, " ", "Passport Number: ", passenger.passport_number)

    elif user_input == 2:
        print("\nYou selected 2. List the flights")

        for flight1 in flights_list:
            count = count + 1
            print(f"\n{count}. Airline: {flight1.plane}, Flight Route: {flight1.flight_route}, "
                            f"Flight Destination: {flight1.destination}, Departure Time: {flight1.time}")

    elif user_input == 3:
        print("\nYou selected: 3. Add passenger to existing flight")
        select_flight = int(input("Please enter a number corresponding to the flight list: > "))

        # But we should iterate over the flight list
        if select_flight == 1:
            print("You Selected", flights_list[select_flight-1].flight_route)
            new_passenger1 =(passenger_list[-1])
            print("Would you like to add", new_passenger1.name, new_passenger1.passport_number, "to Flight",select_flight,"?")

            yes_no = input("y/n: >")
            if yes_no == "y":
#                flights_list[select_flight-1].add_passenger_to_list(new_passenger1) # this adds the passenger, but uses the method
                                                                                            # add_passenger_to_list in Flight()

                flights_list[select_flight-1].flight_passengers_info.append(new_passenger1) # this does the same thing, but without using the method.

                #print("------->", flights_list[select_flight-1].flight_passengers_info)
                print(f"Successfully added {new_passenger1.name} {new_passenger1.passport_number} to Flight {select_flight}")

    elif user_input == 4:
        print("\nYou selected: 4. See Details of a flight")
        user_select_flight = int(input("Please select which flight you want to see the details for? > "))
        if user_select_flight == 1:
            print(f"Airline: {flights_list[user_select_flight - 1].plane}, Flight Route: {flights_list[user_select_flight - 1].flight_route}"
                  f" Flight Destination: {flights_list[user_select_flight - 1].destination},"
                  f"Departure Time:{flights_list[user_select_flight - 1].time},\nPassengers for Flight 1:")

            for flight_one in flights_list[user_select_flight-1].flight_passengers_info:
                print(f"- {flight_one.name}")

            #print("---------->",flights_list[user_select_flight-1].flight_passengers_info)


        # We should list all existing flights (see above)
        # select a flight
        # prom user for input and use some kind of index to select a flight
        # access flight from list using the index
        # create a new passanger objct (see above)

        # run the .add_passanger method on selected flight and
        # pass in the passanger object(it's a variable)