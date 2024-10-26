from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Both Nodes are empty, thus they are the same
        if root1 is None and root2 is None:
            return True
        # One Node is empty and one is not, thus they are not the same
        elif root1 is None or root2 is None:
            return False
        # The values in the nodes are different, thus they are not the same
        elif root1.val != root2.val:
            return False

        # Recursively check if r1 and r2 left/right are the same, or r1 and r2 (flipped) left/right are the same
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
                (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))
