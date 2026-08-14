class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        count = 0

        for i, temp in enumerate(temps):

            while stack and temps[stack[-1]] < temp:
                count += 1
                old_index = stack.pop()
                res[old_index] = i - old_index

            stack.append(i)

        return res