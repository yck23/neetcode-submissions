class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(0, prices[i]-bestbuy, profit)
            bestbuy = min(bestbuy, prices[i])
        return profit