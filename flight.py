from passengers import *

class Flight:
    def __init__(self, plane,flight_route, destination, time):
        self.plane = plane
        self.flight_route = flight_route
        self.flight_passengers_info = []
        self.destination = destination
        self.time = time

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

flights_list = []
flight1 = Flight("British Airways", "London - Amsterdam", "AMS, Netherlands", 1800)
flight2 = Flight("Air France", "Paris - Geneva", "GVA, Switzerland", 1005)
flight3 = Flight("Emirates", "LA - Tokyo", "TKO, Japan", 1800)
flight4 = Flight("Turkish Airlines", "Istanbul - Hurghada", "EGP, Egypt", 2300)

flights_list.append(flight1)
flights_list.append(flight2)
flights_list.append(flight3)
flights_list.append(flight4)