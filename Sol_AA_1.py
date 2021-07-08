no_of_matches = int(input("Enter the number of matches played : "))
no_of_half_centuries = int(input("Enter the number of half centuries scored : "))
skills = input("Enter your skill : ")

if no_of_matches >= 20 or no_of_half_centuries >= 5 or skills == "allrounder":
    print("He/she is eligible for the post of captain")
elif no_of_matches >= 15 or no_of_half_centuries >= 3 or skills == "allrounder":
    print("He/she is eligible for the post of vice-captain")
else:
    print("He/she is not eligible")