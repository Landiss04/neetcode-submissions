class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f = {}

        for num in nums:
            f[num] = f.get(num, 0) + 1
        
        for k,v in f.items():
            if v > 1:
                return True
        return False