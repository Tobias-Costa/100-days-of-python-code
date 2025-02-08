import random

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors ='''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

options = [rock, paper, scissors]
player_choice = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura\n"))
computer_choice = random.randint(0,2)

if player_choice == computer_choice:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nIsso é um empate")
elif player_choice == 0 and computer_choice == 1:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nVocê perdeu")
elif player_choice == 0 and computer_choice == 2:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nVocê ganhou")
elif player_choice == 1 and computer_choice == 0:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nVocê ganhou")
elif player_choice == 1 and computer_choice == 2:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nVocê perdeu")
elif player_choice == 2 and computer_choice == 0:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nVocê perdeu")
elif player_choice == 2 and computer_choice == 1:
    print(f"{options[player_choice]}\nComputador escolheu:\n{options[computer_choice]}\nVocê ganhou")
else:
    print("Você digitou algo errado. Tente novamente.")
