from typing import List


'''
322. Coin Change

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]


sol = Solution()
print(sol.coinChange(coins=[1, 2, 5], amount=11))
# print(sol.coinChange(coins=[2], amount=3))
# print(sol.coinChange(coins=[10, 8, 4, 1, 1], amount=46))
# print(sol.coinChange(coins=[1], amount=0))
# print(sol.coinChange(coins=[2], amount=1))
# print(sol.coinChange(coins=[186, 419, 83, 408], amount=6249))