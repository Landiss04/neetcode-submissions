# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.traverse(root,0, [])
    
    def traverse(self, root,level, ans):
        if root is None:
            return ans
        if level == len(ans):
            ans.append([])
        ans[level].append(root.val)
        self.traverse(root.left, level + 1, ans)
        self.traverse(root.right, level + 1, ans)
        return ans