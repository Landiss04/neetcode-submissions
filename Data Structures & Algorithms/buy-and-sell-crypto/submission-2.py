class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        lo = float('inf')

        for i in range(0, len(prices)):
            lo = min(lo, prices[i])
            maxx = max(maxx, prices[i] - lo)
        return maxx
