class Solution:
    def trap(self, height: List[int]) -> int:
        lo = 0
        hi = len(height) - 1

        left_max = 0
        right_max = 0
        count = 0

        while lo < hi:
            if height[lo] <= height[hi]:
                if height[lo] >= left_max:
                    left_max = height[lo]
                else:
                    count += left_max - height[lo]
                lo += 1
            else:
                if height[hi] >= right_max:
                    right_max = height[hi]
                else:
                    count += right_max - height[hi]
                hi -= 1

        return count