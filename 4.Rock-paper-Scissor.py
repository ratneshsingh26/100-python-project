import random
user_input= int(input("What do you Choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))


##random_no=random.random()
computer_input=random.randint(0,2)
#print(random_no,random_float)
print(user_input,computer_input)
if (user_input,computer_input) in [(0,2),(1,0),(2,1)]:
    print("User Wins")
elif(user_input,computer_input) in [(0,1),(1,2),(2,0)]:
    print("Computer Wins")
else:
    print("It's a Draw!!")