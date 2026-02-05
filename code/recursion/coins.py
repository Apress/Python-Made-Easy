coins_available = [10, 5, 2, 1]
def get_coins(amount, coins_used, max_value):
    if amount == 0:
        print(coins_used)
    for coin_value in coins_available:
        if coin_value <= amount and coin_value <= max_value:
            get_coins(amount-coin_value, 
                     coins_used+[coin_value], 
                     coin_value)

get_coins(amount=15, 
          coins_used=[], 
          max_value=coins_available[0])