# https://trinket.io/features/pygame

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    total_coins = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            total_coins += 1

    if amount > 0:
        print("Não é possível fornecer troco exato com as moedas disponíveis.")
        return None

    return result, total_coins


if __name__ == "__main__":
    coins = list(map(int, input("Insira as moedas disponíveis separadas por espaços: ").split()))
    amount = int(input("Insira o valor que deseja trocar: "))

    change, num_coins = greedy_coin_change(coins, amount)
    if change:
        print(f"Moedas usadas: {change}")
        print(f"Número total de moedas: {num_coins}")
