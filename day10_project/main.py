def art_logo():
    print('''
          
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
          
    ''')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n1 == 0 or n2 == 0:
        print("\n######Erro!######\n")
        calculator()
    else:
        return n1 / n2

def calculator():
    art_logo()
    n1 = float(input("Qual o primeiro número?: "))

    while True: 
        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }

        for key in operations:
            print(key)

        operation_input = input("Escolha uma operação: ")
        n2 = float(input("Qual o próximo número?: "))

        result = operations[operation_input](n1, n2)
        print(f"{n1} {operation_input} {n2} = {result}")

        continue_loop = input(f"Digite 's' para continuar calculando com {result}, ou digite 'n' para iniciar um novo cálculo: ").lower()

        if continue_loop == 's':
            n1 =  result
        else:
            print("\n"*20)
            break

    calculator()

calculator()