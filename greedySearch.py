"""
Find a combination of coins to pay for given price.
Return total number of coins you need.
"""

value = [1,5,10,50,100,500]
coins = [10,20,30,5,10,2]

#The price that coins can provide is up to 2000

price = input();


def solve(price):
    ans = 0

    if (len(value) != len(coins)):
        raise IndexOutOfBoundsException
    for i in range(len(value) - 1, -1, -1):
        t = min( price / value[i], coins[i])
        price -= t * value[i]
        ans += t

    print "Total number of coins is ",ans

if __name__ == "__main__":
    solve(price)
