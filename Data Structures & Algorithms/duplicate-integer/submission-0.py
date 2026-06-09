class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f = {}

        for num in nums:
            f[num] = f.get(num, 0) + 1

        print(f)
        
        for key, value in f.items():
            if value > 1:
                return True
        return False