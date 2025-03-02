print("Bem vindo à calculadora de gorjeta")
bill = float(input("Qual foi o valor total da conta? R$ "))
tip_percentage = float(input("Qual porcentagem de gorjeta gostaria de dar? "))
people_qt = int(input("Quantas pessoas vão dividir a conta? "))
total_per_person = (bill + (bill*(tip_percentage/100))) / people_qt

print(f"Cada pessoa deve pagar: R$ {total_per_person:.2f}")