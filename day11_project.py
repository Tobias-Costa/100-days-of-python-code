import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = [random.choice(cards) for i in range(2)]
computer_cards = [random.choice(cards) for i in range(2)]

user_score = 0
computer_score = 0
end_game_id = 0

def add_user_score():
    global user_score
    user_score = sum(user_cards)

def add_computer_score():
    global computer_score
    computer_score = sum(computer_cards)

def draw_user_card():
    user_cards.append(random.choice(cards))
    add_user_score()

def draw_computer_card():
    computer_cards.append(random.choice(cards))
    add_computer_score()

add_user_score()
add_computer_score()

while True:
    print("Suas cartas:", user_cards, "Pontuação:", user_score)
    print("Cartas do computador:", [computer_cards[0], "X"])

    if user_score == 21:
        print("Você ganhou!")
        end_game_id = 1
        break
    elif computer_score == 21:
        print("Você perdeu.")
        end_game_id = 1
        break
    elif user_score == 21 and computer_score == 21:
        print("Empate")
        end_game_id = 1
        break

    if user_score > 21:
        if 11 in user_cards:
            user_cards[user_cards.index(11)] = 1  
            add_user_score()
            if user_score > 21:
                print("Você perdeu.")
                end_game_id = 1
                break
        else:
            print("Você perdeu.")
            end_game_id = 1
            break
    draw_card =  input("Você deseja pegar outra carta?[S/N]\nResposta: ").strip().lower()
    if draw_card == "s":
        print('\n' * 2)
        draw_user_card()
    else:
        print('\n' * 2)
        break


if end_game_id == 0:
    while computer_score < 17:
        draw_computer_card()

    print("Cartas do computador:", computer_cards)
    print("Pontuação do computador:", computer_score)

    if computer_score > 21:
        print("Você ganhou!")
    elif user_score > computer_score:
        print("Você ganhou!")
    elif user_score < computer_score:
        print("Você perdeu.")
    else:
        print("Empate")

#Criar função para jogar novamente