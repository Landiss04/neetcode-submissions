class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        max_count = 0

        if len(nums) == 0:
            return 0
        else:
            temp_count = 1

        for i in range(0, len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1

        for num in freq:
            temp_count = 1
            current = num

            while current + 1 in freq:
                temp_count += 1
                current += 1

            max_count = max(max_count, temp_count)

        return max_count