class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.stack = []
        def find(node):
            if not node:
                return
            if not node.left and not node.right:
                self.stack.append(node.val)
            elif node.left:
                find(node.left)
            elif node.right:
                find(node.right)
        find(root)
        return self.stack.pop()