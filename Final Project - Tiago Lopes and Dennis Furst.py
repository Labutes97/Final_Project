# Basic Track Assessment
# Work done by Tiago Lopes and Dennis Furst

# Please use the following capitals as a shortcut, as you can use them all at once when answering the input. So, you
# don't have to write them one by one. NO SPACES AFTER THE COMMA.
# Kabul,Tirana,Algiers,Andorra la Vella,Luanda,Saint John's,Buenos Aires,Yerevan,Canberra,Vienna,Baku,Nassau,
# Manama,Dhaka,Bridgetown,Minsk,Brussels,Belmopan,Porto-Novo,Thimphu,Sarajevo,Gaborone,Brasilia,Sofia,Ouagadougou,
# Gitega,Praia,Phnom Penh,Yaounde,Ottawa,Bangui,N'Djamena,Santiago,Beijing,Bogotá,Moroni,Kinshasa,San Jose,Zagreb,
# Havana,Nicosia,Prague,Copenhagen,Roseau,Santo Domingo,Quito,Cairo,San Salvador,Asmara,Tallinn,Suva,Helsinki,Paris,
# Libreville,Banjul,Tbilisi,Berlin,Accra,Athens,Saint George's,Guatemala,Conakry,Bissau,Georgetown,Port-au-Prince,
# Tegucigalpa,Budapest,Reykjavik,New Delhi,Jakarta,Tehran,Baghdad,Dublin,Jerusalem,Rome,Kingston,Tokyo,Amman,Nur-Sultan,
# Nairobi,Tarawa,Pristina,Kuwait City,Bishkek,Vientiane,Riga,Beirut,Maseru,Monrovia,Tripoli,Vaduz,Vilnius,Luxembourg,

# Collect terms
terms = []
total_suggestions = 0
minimum_suggestions = 50

import os.path
if os.path.isfile("List Of Capitals.txt"):

    with open("List Of Capitals.txt", "r") as my_file:
        next(my_file)
        all_capitals = my_file.read().splitlines()

    input_message = input("There are already the following capitals in the pool:\n"
                          + ", ".join(all_capitals) +
                          "\n\nType '1' if you want to play with the existing pool"
                          "\nType '2' if you want to add new capitals to the pool"
                          "\nType '3' if you want to create your own pool")

    if input_message == "1":
        print("\nLet's proceed!")

    elif input_message == "2":
        while True:
            new_capital = input("\nPlease suggest new capitals to add to the pool!\n"
                                "Write '0' and press Enter once you are done. Thanks!")
            if new_capital != "0":
                with open("List Of Capitals.txt", "a") as my_file:
                    if new_capital not in all_capitals:
                        my_file.write("\n" + new_capital)
                        print("\nYou have added: " + new_capital)
                    else:
                        print("\nThis capital is already in the pool. Please pick another one or exit.")
            else:
                break

    else:
        print("\nWelcome to Bingo! Let's begin.\n\n"
              "Suggest different capitals to add to the pool.\n"
              "You have two options:\n"
              "1) Add the capitals separated by a ',' (e.g., Lisbon,Paris);\n"
              "2) Add one capital at the time.\n")

        while minimum_suggestions > total_suggestions:
            suggestion = input("Please provide a minimum of 50 capitals!")

            suggestions = suggestion.split(",")
            for capital in suggestions:
                terms.append(capital)
            total_suggestions = len(terms)
            if total_suggestions > minimum_suggestions:
                print("\nWe have at least 50 capitals!")
            else:
                print("\nAlmost there! You need", minimum_suggestions - total_suggestions, "more capitals!\n")

        with open("List Of Capitals.txt", "w") as my_file:
            my_file.write("Names of the capitals:\n")
            for term in terms:
                my_file.write(term + "\n")

# Sorry about the duplicated code, didn't know any better...
else:
    print("\nWelcome to Bingo! Let's begin.\n\n"
          "Suggest different capitals to add to the pool.\n"
          "You have two options:\n"
          "1) Add the capitals separated by a ',' (e.g., Lisbon,Paris);\n"
          "2) Add one capital at the time.\n")

    while minimum_suggestions > total_suggestions:
        suggestion = input("Please provide a minimum of 50 capitals!")

        suggestions = suggestion.split(",")
        for capital in suggestions:
            terms.append(capital)
        total_suggestions = len(terms)
        if total_suggestions > minimum_suggestions:
            print("\nWe have at least 50 capitals!")
        else:
            print("\nAlmost there! You need", minimum_suggestions - total_suggestions, "more capitals!\n")

    with open("List Of Capitals.txt", "w") as my_file:
        my_file.write("Names of the capitals:\n")
        for term in terms:
            my_file.write(term + "\n")

# Bingo card
import random

while True:
    with open("List Of Capitals.txt") as my_file:
        next(my_file)
        all_capitals = my_file.read().splitlines()

    bingo_card = random.sample(all_capitals, 25)
    print("\nLet's get you a card!\n")
    print(bingo_card)
   # cards = "\n".join([", ".join(bingo_card[i:i + 5]) for i in range(0, len(bingo_card), 5)])
    # cards.split("")

    bingo_card_message = input("\nAre you happy with your card?"
                               "\n1) If you want another card press 'A'; "
                               "\n2) If you are OK with your current card press Enter.")
    if bingo_card_message == "A":
        continue
    else:
        break

# Draw terms
draw_capitals = random.sample(all_capitals, len(all_capitals))

print("\nWe will know begin with drawing the terms from the pool!")

for draw_capital in draw_capitals:
    drawing_message = input("\nThis is the capital: " + draw_capital +
                            "\n\n1) Press Enter to see the next one!"
                            "\n2) Type 'Y' if you have one of the capitals in your card"
                            "\n3) Type 'Q' if you want to quit the game")

    if drawing_message == "":
        continue
    elif drawing_message == "Y":
        if draw_capital in bingo_card:
            bingo_card.remove(draw_capital)
            if len(bingo_card) == 0:
                print("\nCongratulations you won!")
                break
            else:
                print("\nCongratulations! We have removed one capital."
                      "\nThese are your remaining capitals:\n\n", bingo_card)
        else:
            print("\nPlease check more carefully next time. Your card did not have that capital.\n"
                  "Please see the new capital:\n\n", bingo_card)
    elif drawing_message == "Q":
        print("\nHope to see you again!")
        break




