class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx = 0
        f = {}

        if len(nums) == 0:
            return 0

        for num in nums:
            f[num] = f.get(num, 0) + 1

        for k, v in f.items():
            i = k+1
            temp = 1
            while i in f:
                temp += 1
                i += 1
            maxx = max(maxx, temp)

        return maxx
            
