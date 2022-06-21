"""
314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

from collections import deque
from collections import defaultdict

# Step 1: Implement base node class

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self. right = None

# Implement Solution class
class Solution:
    def verticalOrder(self, root):

        # Base Condition
        if root is None:
            return []

        # Initialization

        column_map = defaultdict(list)
        queue = deque([(0,root)])
        min_hD = float('inf')
        max_hD = float('-inf')

        result = []

        while queue:

            hD, node = queue.popleft()

            column_map[hD].append(node.val)
            min_hD = min(hD, min_hD)
            max_hD = max(hD, max_hD)

            if node.left:
                queue.append((hD - 1, node))

            if node.right:
                queue.append((hD + 1, node))

        for x in range(min_hD, max_hD + 1):
            result.append(column_map[x])

        return result




