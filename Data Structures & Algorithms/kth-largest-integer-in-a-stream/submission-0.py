class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.ans = sorted(nums)
        self.t = k

    def add(self, val: int) -> int:
        self.ans.append(val)
        self.ans.sort()
        return self.ans[-self.t]