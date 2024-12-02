from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        current_min = prices[0]
        max_profit = 0
        for val in prices:
            if val < current_min:
                current_min = val
            max_profit = max(max_profit, val - current_min)

        return max_profit
