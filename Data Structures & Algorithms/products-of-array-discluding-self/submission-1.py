class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        res = [0] * len(nums)

        pre[0], post[len(post)-1] = 1,1

        for i in range(1, len(pre)):
            pre[i] = nums[i-1] * pre[i-1]
        for i in range(len(res)-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]
        for i in range(len(res)):
            res[i] = post[i] * pre[i]
        return res

