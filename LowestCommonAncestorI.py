class LowestCommonAncestorI:
    def lowestCommonAncestorI(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestorI(root.left, p, q)
        right = self.lowestCommonAncestorI(root.right, p, q)

        if left and right:
            return root

        if left is None:
            return right
        if right is None:
            return left
