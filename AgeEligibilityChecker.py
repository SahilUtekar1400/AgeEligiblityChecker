print("Please check your eligibility for the upcoming election's!")
age = int(input("What is your age?"))

if age >= 18:
    voter_card = input("Do you have a voter card? enter Y for Yes and N for No?")
    if voter_card.lower() == "y":
        print("You are eligible for the upcoming election voting!")

    elif voter_card.lower() == "n":
        print("You are 18 and above!. However, you are required to apply for the voter card to become eligible for voting!")

    else:
        print("You have inputted wrong field for the voter id!")

else:
    print("You are ineligible for the voting!")