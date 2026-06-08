class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.traverse(root)
        return self.diameter
    
    def traverse(self, root):
        if root is None:
            return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        self.diameter = max(self.diameter, left + right)
        
        return 1 + max(left, right)