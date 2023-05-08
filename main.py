get_name = input("What's your name? \n")

print("Hello " + get_name + "! \nWelcome to the band name generator!")

get_city = input("What's your city? \n").capitalize()
get_pet_name = input("What's your pet's name? \n").capitalize()

if len(get_city) > 6:
    get_city = get_city[slice(5)]

print("Your super band name is: " + get_city +  " " + get_pet_name)