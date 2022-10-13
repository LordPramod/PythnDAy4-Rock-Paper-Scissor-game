
# # rand_num = input("Enter a random number")
# # random.seed(rand_num)
# # names_string = input("give me every bodys name ")
# # name = names_string.split(", ")
# #
# # # num_items = len(name)
# # # random_name = random.randint(0 , num_items - 1)
# # # person_who_will_pay_bill = name[random_name]
# # # print(person_who_will_pay_bill)
# # random_choice = random.choice(name)
# # print(random_choice + "is going to pay today")
# # Split string method
#
# #
# # names_string = input("Give me everybody's names, separated by a comma. ")
# # names = names_string.split(",")
# #
# # loser = random.sample(names, 1)
# # print(f'{loser[0]} is going to buy the meal today!')
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("Enter Where do you want to put The treasure")
# h = int(position[0])
# v = int(position[1])
# map[h-1][v-1]="X"
# print(f"{row1}\n{row2}\n{row3}\n")

print("Welcome to rock paper Game")
game_rule=["Rock","Paper","Scissor"]
user_choice = int(input("Enter You choice 0 for Rock, 1 for Paper, and 2 for Scissor"))
print(user_choice)
print(f"You choose:\t {game_rule[user_choice]}")
import random
computer_choice = random.randint(0, 2)
print(f"Computer Choice:\t{game_rule[computer_choice]}")
if user_choice>=3:
    print("Enter a valid choice")
elif user_choice==0 and computer_choice==2:
    print("You Win")
elif computer_choice==0 and user_choice == 2:
    print("You Loose")
elif user_choice > computer_choice:
    print("You Win")
elif user_choice < computer_choice:
    print("You loose")
elif user_choice == computer_choice:
    print("Its a draw")



