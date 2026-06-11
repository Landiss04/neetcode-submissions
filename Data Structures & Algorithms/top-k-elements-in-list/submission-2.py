class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        ans = []

        for num in nums:
            f[num] = f.get(num, 0) + 1

        for _ in range(k):
            key = max(f, key=f.get)
            ans.append(key)
            f.pop(key)

        return ans