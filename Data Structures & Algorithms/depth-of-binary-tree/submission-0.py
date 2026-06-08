from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.traverse(root.left, 1), self.traverse(root.right, 1))

    def traverse(self, root, count):
        if root is None:
            return count
        count += 1
        return max(
            self.traverse(root.left, count),
            self.traverse(root.right, count)
        )