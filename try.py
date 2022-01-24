class cinema():
    def __init__(self, capacity):
        self.capacity = capacity
        self.people = []
    
    def add_People(self, name):
        if not self.check():
            return False
        self.people.append(name)
        return True

    def check(self):
        return self.capacity - len(self.people)
        

Atrium = cinema(4)
lists = ["A", "B", "C", "D", "E"]

for i in lists:
    answer = Atrium.add_People(i)
    if answer:
        print(f"A seat has been allocated for {i}")
    else:
        print(f"There is no seat for {i}")

#  class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passangers = []
    
#     def add_passenger(self, name):
#         if not self.open_seats():
#             print(False)
#             return False
#         self.passangers.append(name)
#         print(True)
#         return True
    
#     def open_seats(self):
#         return self.capacity - len(self.passangers)

# flight = Flight(3)
# lists = ["A", "B", "C", "D"]
# for person in lists:
#     answer = flight.add_passenger(person)
#     if answer:
#         print(f"Added {person} to the flight successfully.")
#     else:
#         print(f"No available seat for {person}.")