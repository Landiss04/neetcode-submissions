class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_count = 1

        if len(nums) == 0:
            return 0

        f = {}

        for num in nums:
            f[num] = f.get(num, 0) + 1

        maxx = 0

        for key, value in f.items():
            while key + 1 in f:
                temp_count += 1
                key += 1 

            maxx = max(maxx, temp_count)
            temp_count = 1

        return maxx