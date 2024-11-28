#!/usr/bin/python3
"""
Use Greedy approach to find least number of coins.
"""


def makeChange(coins, total):
    """
    Use Greedy approach to find least number of coins.
    """
    # If total less than or eq to 0
    if total <= 0:
        return 0

    # Sort list of coins to lead with the highest
    coins.sort(reverse=True)
    coin_num = 0

    # Loop over each coin
    for coin in coins:
        if total == 0:
            break

        # Find how many of current coin can fit in total
        coin_num += total // coin

        # Find remainder and set total to remainder after coins used
        total %= coin

    return coin_num if total == 0 else -1
