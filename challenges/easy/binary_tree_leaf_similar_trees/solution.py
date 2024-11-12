from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root: TreeNode, leaf_list: List):
            if not root:
                return
            if not root.left and not root.right:
                leaf_list.append(root.val)
                return

            get_leaves(root.left, leaf_list)
            get_leaves(root.right, leaf_list)

        leaves1, leaves2 = [], []
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)
        return leaves1 == leaves2
