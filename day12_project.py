import random

def art():
    print('''

              _ _       _       _                   
     /\      | (_)     (_)     | |                  
    /  \   __| |___   ___ _ __ | |__   ___    ___   
   / /\ \ / _` | \ \ / / | '_ \| '_ \ / _ \  / _ \  
  / ____ \ (_| | |\ V /| | | | | | | |  __/ | (_) | 
 /_/  _ \_\__,_|_| \_/ |_|_| |_|_| |_|\___|  \___/  
 | \ | |                                            
 |  \| |_   _ _ __ ___   ___ _ __ ___               
 | . ` | | | | '_ ` _ \ / _ \ '__/ _ \              
 | |\  | |_| | | | | | |  __/ | | (_) |             
 |_| \_|\__,_|_| |_| |_|\___|_|  \___/              
                                                    
                                                                                         
''')
    
def game():
    attempts = 0

    art()
    print("Bem-vindo ao Jogo de Adivinhação de Números!")
    print("Estou pensando em um número entre 1 e 100.")

    difficulty = input("Escolha uma dificuldade. Digite 'facil' ou 'dificil': ")
    if difficulty == 'facil':
        attempts = 10
    else:
        attempts = 5
    
    number = random.randint(1,100)

    while attempts != 0:
        
        print(f"Você tem {attempts} chances restantes para acertar o número")
        n_guess = int(input("Chute um número: "))

        if n_guess > number:
            print("Muito alto!\nChute novamente.")
            attempts -= 1
        elif n_guess < number:
            print("Muito baixo!\nChute novamente.")
            attempts -= 1
        else:
            print("\nParabéns você acertou o número! :)")
            break

        if attempts == 0:
            print(f"\nVocê perdeu. :(\nO número correto era {number}")
        
game()