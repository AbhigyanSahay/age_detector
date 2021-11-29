print("Hello! Welcome to the Age Detector Program.")
print("This program's features :- ")
print("You can get to know the age of yours.")
print("You can get to know that in a specific year, what will be your age.")

cur_year = int("2021")
birth_year = int(input("Enter your year of birth: "))


while cur_year >= birth_year:
    age = cur_year - birth_year
    
    if cur_year-birth_year <= 3:
        print("Sorry! This app is for people aged 3+")
        exit()
    else:
        print(f"Your current age is {age} years.")
        print("Enter 'y' for yes or 'n' for no to know your age for a spcific year")
        age_knowing_choice = str(input())
        if age_knowing_choice == 'y':
            age_knowing_year = int(input("Enter the year: "))
            specific_year_age = (age_knowing_year-birth_year)
            print(f"Your age in the year {age_knowing_year} will be {specific_year_age} years.")
            print("\nThank You")
            exit()
            
            
        elif age_knowing_choice == 'n':
            print("OK, Thanks")
        else:
            print("Invalid Input")
