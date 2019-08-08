class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lst = []
        if root is None:
            return lst
        else:
            for child in root.children:
                lst.extend(self.postorder(child))
            lst.append(root.val)
        return lst