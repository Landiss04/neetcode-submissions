class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lo = prices[0]
        temp_max = 0
        for i in range(1, len(prices)):
            lo = min(lo, prices[i])
            temp_max = prices[i] - lo
            maxP = max(temp_max, maxP)
        return maxP

        