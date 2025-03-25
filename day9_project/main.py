#Setup
bid_dictionary = {}

#Looping inputs
while True:
    name = input("Digite o nome do licitante:\n")
    bid = int(input("Digite o valor do lance:\nR$ "))

    bid_dictionary[name] = bid

    should_continue = input("Há outro licitante que quer dar lance?[Y/N]\n").lower()
    if should_continue == "y":
        print("\n" * 20)
        continue
    elif should_continue == 'n':
        break

#Achando licitante com maior lance
max_bidder = max(bid_dictionary, key=bid_dictionary.get)
max_bid = bid_dictionary[max_bidder]

print(f"O ganhador é {max_bidder} com um lance de R${max_bid}")

