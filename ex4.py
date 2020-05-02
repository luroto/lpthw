# The first variable, yay!
cars = 100
# try a 4 instead a 4.0 and got a different result in carpool_capacity
space_in_a_car = 4.0
# Another variable
drivers = 30
# Another variable
passengers = 90
# Testing out type of results
cars_not_driven = cars - drivers
# Another one
cars_driven = drivers
# We got a different result here when we use 4 instead of 4.0
carpool_capacity = cars_driven * space_in_a_car
# Final comment!
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car,
      "in each car.")

# A name error will rise if some variable is misspelled
# If I use a 4.0 instead of 4, all the operations that involved the 4.0 will produce a float result
# print is a function for printing to console whatever you put in brackets
# float is for specify the type of data you're going to enter
