class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node):
            if node == None:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.diameter = max(self.diameter, left+right)
            return max(left, right) + 1

        self.diameter = 0
        height(root)
        return self.diameter