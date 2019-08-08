class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, lst):
            if root == None:
                return lst
            if root.left:
                if root.left.left or root.left.right:
                    helper(root.left,lst)
                else:
                    lst.append(root.left.val)
            if root.right:
                helper(root.right, lst)
        lst1 = []
        helper(root, lst1)
        return sum(lst1)