class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        if not root:
            return 0
        def path(node, target):
            if not node:
                return 0
            left = path(node.left, node.val)
            right = path(node.right, node.val)
            self.result = max(self.result, left + right)
            if node.val != target:
                return 0
            return 1 + max(left, right)
        path(root, root.val)
        return self.result