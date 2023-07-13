value = float(input())


def coins(value):
    print("NOTAS:")
    notes = [100, 50, 20, 10, 5, 2]
    for note in notes:
        quantity = int(value / note)
        value = value % note
        print(f"{quantity} nota(s) de R$ {note:.2f}")

    print("MOEDAS:")
    coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    for coin in coins:
        quantity = int(value / coin)
        value = round(value % coin, 2)
        print(f"{quantity} moeda(s) de R$ {coin:.2f}")


coins(value)
