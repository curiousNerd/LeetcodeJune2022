class Node:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):

        # Base Condition

        if root is None:
            return None

        # Searching

        if root == p or root == q:
            return root

        # Traverse

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Find LCA

        if left and right:
            return root

        return left if left is not None else right