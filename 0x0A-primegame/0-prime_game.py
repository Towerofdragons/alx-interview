#!/usr/bin/python3
"""
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and
removing that number and
its multiples from the set. The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    Find the winner of most games.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to find the highest prime list
    max_num = max(nums)

    # Sieve of Erastothenes
    # Find the prime numbers up to prime_nums
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Start game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Assuming Maria always goes first
        # If the number of primes up to n is odd, Maria wins;
        # otherwise, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Compare final wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
