# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve
# any profit, return 0.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        unique_prices = [prices[0]]
        temp = prices[0]
        for i in range(1, len(prices)):
            if temp != prices[i]:
                temp = prices[i]
                unique_prices.append(prices[i])
        res = [0]
        step = 0
        l = len(unique_prices)
        if l > 1:
            max_price = max(unique_prices)
            while step < l:
                min_price = unique_prices[step]
                if max_price == unique_prices[step-1]:
                    max_price = max(unique_prices[step:])
                r = max_price - min_price
                if r > 0:
                    res.append(r)
                step += 1
            return max(res)
        else:
            return 0
