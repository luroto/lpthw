# Setting a first variable
types_of_people = 10
# Creating a string using this variable
x = f"There are {types_of_people} types of people."

#Setting two more variables
binary = "binary"
do_not = "don't"
# Another string using variables and f option
y = f"Those who know {binary} and those who {do_not}."

# setting variables
print(x)
print(y)

# printing strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# using the format option for the first time on this course
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

# adding two strings
print(w + e)
