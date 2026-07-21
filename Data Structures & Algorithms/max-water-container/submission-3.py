class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxx = 0
        l,r = 0, len(h) - 1

        while l < r:
            area = (r-l) * min(h[l],h[r])
            maxx = max(maxx, area)
            if h[l] < h[r]:
                l +=1 
            else:
                r -= 1
        return maxx




