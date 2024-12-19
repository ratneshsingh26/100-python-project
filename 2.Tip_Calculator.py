print("Welcome to the tip calculator!\n")
total_bill=float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_amount=total_bill*(tip_percentage/100)
splitted_bill=(tip_amount+total_bill)/number_of_people
print(f"Each Person should pay: ${round(splitted_bill,2)}")