import random
user_input=input("Enter your choice (0 for Rock,1 for Paper,2 for Scissors)")
com_choice=random.randint(0,2)
user_choice=int(user_input)
if user_choice >=3 or user_choice <0 :
    print("you entered invalid num.you lose")
else :
    print(f"Your choice is {user_input}")
    print(f"Computer choice is {com_choice}")
    if user_choice==com_choice :
        print("The match is draw")
    elif user_choice==0 and com_choice==2 :
        print("You wins")
    elif user_choice==2 and com_choice==0 :
        print("You lose")
    elif com_choice>user_choice :
        print("You lose")
    elif user_choice>com_choice :
        print("you wins")


