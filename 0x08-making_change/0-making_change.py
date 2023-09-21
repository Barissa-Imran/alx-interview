#!/usr/bin/python3
"""
making_change interview question
"""


def makeChange(coins, total):
    """
    function for making change algorithm
    """
    if total <= 0:
        return 0

    # create an array to store the min number of --
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # update the min number of coins req for each value
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # return the min number of coins required to reach the total value
    return min_coins[total] if min_coins[total] != float('inf') else -1
