# imports

from collections import deque
from collections import defaultdict


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def verticalOrder(self, root):

        # Base case
        if root is None:
            return []

        # initializations

        queue = deque([(0, root, 0)])
        col_dict = defaultdict(list)
        result = []

        min_hD = float('inf')
        max_hD = float('-inf')

        # code

        while queue:

            hD, node, vD = queue.popleft()

            col_dict[hD].append((vD, node.val))

            min_hD = min(hD, min_hD)
            max_hD = max(hD, max_hD)

            if node.left:
                queue.append((hD - 1, node.left, vD + 1))

            if node.right:
                queue.append((hD + 1, node.val, vD + 1))

        for hD in range(min_hD, max_hD + 1):
            val = [i[1] for i in sorted(col_dict[hD])]
            result.append(val)

        return result
