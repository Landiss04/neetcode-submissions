class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0

        for i in range(0 ,len(prices)):
            if i + 1 < len(prices):
                maxx = max(maxx, max(prices[i+1:]) - prices[i])

        return maxx