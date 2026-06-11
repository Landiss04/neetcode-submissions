# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.search(root, root.val)

    def search(self, root, maxx):
        if not root:
            return 0
        
        count = 1 if root.val >= maxx else 0
        maxx = max(maxx, root.val)

        return count + self.search(root.left, maxx) + self.search(root.right, maxx)