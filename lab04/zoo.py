def show_help():
    print("Type 'help' to get a list of all the things you can do")
    print("Type 'see' to get a list of all the animals")
    print("Type 'pet' followed by the animal's name to pet a particular animal")
    print("Type 'bye' to leave the zoo and exit the program")


def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")


def pet_animal(animal):
    if animal == "Clover":
        print("Clover is so happy! ❤️")
    elif animal == "Coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "Arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    else:
        print("Sorry, I don't know that animal")


print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()


keep_going = True#keeps the program going so you don't have to keep using python zoo.py
while keep_going:
    response = input("What would you like to do? ") #response has to be inside the while loop
    if response == "help":
        show_help()
    elif response == "see":
        show_all_animals()
    elif response.startswith("pet "): #user starts by typing pet
        animal = response[4:] #after the first four characters 'pet '
        pet_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        keep_going = False
    else:
        print("Sorry, I don't understand that command")