import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = True

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

def art():
    print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      '------'                           |__/           
''')

while play_again:
    print('\n' * 20)
    art()
    user_cards = []
    computer_cards = []

    user_score = 0
    computer_score = 0
    end_game_id = 0


    user_cards = [random.choice(cards) for i in range(2)]
    computer_cards = [random.choice(cards) for i in range(2)]
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
                print("Ufa! Você tirou um Ás. Ele pode ser convertido para uma carta de valor 1 ou 11.\nAtualizando sua pontuação para a melhor estratégia...")
                print('\n')
                print("Suas cartas:", user_cards, "Pontuação:", user_score)
                print("Cartas do computador:", [computer_cards[0], "X"])
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
            
        print("Suas cartas:", user_cards, "Pontuação:", user_score)
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
    
    play_again_question = input("Você deseja jogar novamente?[S/N]\nResposta: ").strip().lower()
    if play_again_question != "s":
        play_again = False

print("Obrigado por jogar! :)")