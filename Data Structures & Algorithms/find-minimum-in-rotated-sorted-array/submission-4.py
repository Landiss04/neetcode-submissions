class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        smallest = 1001
        if len(nums) == 1:
            return nums[0]

        while l < r:
            smallest = min(smallest, nums[l], nums[r])
            l += 1
            r -= 1
        
        if len(nums) % 2 == 1: #number is odd
            r += 1
            return min(smallest, nums[r-1])

        return smallest

        #l ---->    <---- r

