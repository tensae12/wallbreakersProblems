class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root, lst):
            if root is None:
                return
            if root.left is None or root.right is None:
                lst.append(root.val)
            helper(root.right,lst)
            helper(root.left, lst)
        leaf_seq1 = []
        leaf_seq2 = []
        helper(root1, leaf_seq1)
        helper(root2, leaf_seq2)
        return leaf_seq1 == leaf_seq2