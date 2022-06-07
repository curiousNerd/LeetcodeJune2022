
class Node:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:

    def LCA_Sol_1(self, p: Node, q: Node):

        seen = set()

        # Traverse up on one node (p) and keep storing nodes in a Set

        while p:

            seen.add(p)

            p = p.parent

        # Traverse up the second node (q) and return as soon as first match is found in the set. That is LCA

        while q:

            if q in seen:
                return q
            q = q.parent


    def LCA_Sol_2(self, p: Node, q: Node):

        p_copy = p
        q_copy = q

        while p_copy != q_copy:

            p_copy = p_copy.parent if p_copy else q
            q_copy = q_copy.parent if q_copy else p

        return p_copy
