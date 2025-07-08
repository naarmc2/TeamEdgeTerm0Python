def mad_lib():
    type_of_day = input("What type of day is it? ")
    place = input("Where is this situated? ")
    person = input("Who dis? ")
    item = input("What item? ")
    caller = input("Who called? ")
    pet_type = input("What type of pet? ")
    pet_name = input("What's the pet's name? ")
    exclaim = input("What does the person say in response? ")
    magical_item = input("What's the special item? ")



    print(f"It was a {type_of_day} day on the West Coast. Many people were out and about on the {place}.\n {person} had went out to buy a {item}. They received a call from {caller} telling them that their \n pet {pet_type} {pet_name} was missing \n '{exclaim}' he/she exclaimed. Then using their {magical_item} they teleported back home.")


def main():
   mad_lib()

main()