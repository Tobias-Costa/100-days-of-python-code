from hangman import hangman_ascii as hangman_stage
from game_ascii import ps_ascii
from words_list import word

def play_again():
    print('-'*30)
    yes_or_no = input("Deseja jogar novamente? [Y/N] ").upper()
    if yes_or_no == "Y":
        main()
    elif yes_or_no == "N":
        print(f"{'>'*7} Obrigado por jogar! {'<'*7}")
    else:
        print("Algo que digitou está incorreto.")
        play_again()


def main():
    correct_letters = []
    blank = "_"
    display = ""
    lifes = 6
    choosen_word = word()

    ps_ascii()
    print(f"{'>'*7} Seja bem vindo ao jogo da forca!!! {'<'*7}")

    for i in range(len(choosen_word)):
        display += blank

    while True:
        print(hangman_stage()[lifes])
        print(f"{display}\n")

        if display == choosen_word:
            print("Você ganhou!")
            play_again()
            break
        elif lifes == 0:
            print("Game Over!!!")
            print(f"A palavra era: {choosen_word}")
            play_again()
            break

        guess = input("Chute uma letra: ").lower()
        if guess in choosen_word:
            display = ""
            for letter in choosen_word:
                if letter in correct_letters:
                    display += letter
                elif letter == guess:
                    display += letter
                    correct_letters.append(guess)
                else:
                    display += blank
        else:
            lifes -= 1

main()
    
    









