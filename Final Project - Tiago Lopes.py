# Basic Track Assessment
# Work done by Tiago Lopes (S4015258)

# Collect terms
terms = []
total_suggestions = 0
minimum_suggestions = 3
message = ""

import os.path


try:
    with open("List Of Capitals.txt") as my_file:
        print("File found")
except FileNotFoundError:
    print("File not found")



while minimum_suggestions != total_suggestions:
    suggestion = str(input("Suggest different capitals to add to the pool. \n"
                           "Please provide a minimum of 30 capitals!"))
    total_suggestions += 1
    terms.append(suggestion)

message += "We have all the 30 capitals!"
print(message)  # Shouldn't I be able to just display the message. Not sure if print is the best option
print(terms)

with open("List Of Capitals.txt", "w") as my_file:
    my_file.write("Names of the capitals:\n\n")
    for term in terms:
        my_file.write(term + "\n")

# Draw terms
import random
with open("List Of Capitals.txt") as my_file:
    next(my_file)
    all_capitals = my_file.read().split()

random_capitals = random.sample(all_capitals, 2)
print(random_capitals)

for random_capital in random_capitals:
    drawing_message = input("This is the capital: " + random_capital +  # Maybe add something to automatically change to first capital
                            "\nPress Enter to see the next one!")  # second capital,...

# Bingo card


