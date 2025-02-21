import random

def word():

    words =[
    "abacaxi", "escola", "computador", "camelo", "cachorro",
    "elefante", "girafa", "tigre", "gato", "cavalo",
    "mesa", "cadeira", "janela", "porta", "parede",
    "rio", "montanha", "floresta", "oceano", "ilha",
    "livro", "caderno", "lapis", "caneta", "borracha",
    "verde", "azul", "vermelho", "amarelo", "roxo",
    "carro", "avião", "barco", "bicicleta", "moto",
    "fruta", "banana", "melancia", "morango", "manga",
    "chave", "luz", "tomada", "energia", "fone",
    "trabalho", "cidade", "campo", "praia", "estrada"
    ]

    return random.choice(words)