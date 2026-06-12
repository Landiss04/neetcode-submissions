# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.find(root, ans, 0)
        return ans

    def find(self, root, ans, depth):
        if not root:
            return None
        
        if depth == len(ans):
            ans.append(root.val)
        
        self.find(root.right, ans, depth + 1)
        self.find(root.left, ans, depth + 1)

    

        