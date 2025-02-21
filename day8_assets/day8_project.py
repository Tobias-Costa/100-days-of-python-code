from art import logo

def play_again():
    print('-'*30)
    yes_or_no = input("Deseja continuar? [Y/N] ").upper()
    if yes_or_no == "Y":
        main()
    elif yes_or_no == "N":
        print(f"{'>'*7} Adeus! {'<'*7}")
    else:
        print("Algo que digitou está incorreto.")
        play_again()

def caesar_cipher(original_text, shift_amount, direction):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    code_word = ""
    
    if direction ==  "decodificar":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            code_word += letter
        else:
            shifted_position = (alphabet.index(letter)+shift_amount) % len(alphabet) 
            code_word += alphabet[shifted_position]

    print(f"Aqui está o resultado do processo: {code_word}")

def main():
    direction = ""
    while direction != "codificar" and direction != "decodificar":
        direction = input("Digite 'codificar' para criptografar ou 'decodificar' para descriptografar.\n ")
    text = input(f"Digite o texto que deseja {direction}.\n").lower()
    shift_amount =  int(input("Digite o número de deslocamento.\n"))
    caesar_cipher(text, shift_amount, direction)
    play_again()

            
logo()
main()