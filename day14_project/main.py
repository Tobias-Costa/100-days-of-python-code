from random import choice
from art import logo, vs
from game_data import data

CLEAR_TERMINAL = '\n' * 20

game_over = False
score = 0

print(logo)
p1_dict = choice(data)

def format_data(personality):
    """Formata as informações prestadas dentro do dicionário das personalidades e retorna em um formato printável"""
    p_name = personality['name']
    p_description = personality['description']
    p_country = personality['country']
    return f"{p_name}, um(a) {p_description}, país de origem: {p_country}."

def check_solution(guess, p1_followers, p2_followers):
    """Pega o chute do player e os seguidores das personalidades e retorna se o seu chute estava certo ou errado"""
    if p1_followers > p2_followers:
        return guess == 'a'
    else:
        return guess == 'b'

while game_over is not True:

    p2_dict = choice(data)
    while not p2_dict != p1_dict:
        p2_dict = choice(data)
    
    print(f"Compare A: {format_data(p1_dict)}")
    print(vs)
    print(f"Contra B: {format_data(p2_dict)}")

    player_guess = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower()
    
    p1_followers = p1_dict['follower_count']
    p2_followers = p2_dict['follower_count']
    is_correct = check_solution(player_guess, p1_followers, p2_followers)

    if is_correct:
        score += 1
        p1_dict = p2_dict
        print(CLEAR_TERMINAL)
        print(logo)
        print(f"Parabéns! Você acertou. Sua pontuação agora é: {score}.")
    else:
        print(CLEAR_TERMINAL)
        print(logo)
        print(f"Desculpa, você errou. Pontuação final: {score}.")
        game_over = True
