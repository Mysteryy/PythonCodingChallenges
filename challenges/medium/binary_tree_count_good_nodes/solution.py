class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helperFunc(node: TreeNode, max_val):
            counter = 0
            if not node:
                return counter
            if node.val >= max_val:
                counter += 1
            max_val = max(max_val, node.val)

            return counter + helperFunc(node.left, max_val) + helperFunc(node.right, max_val)

        return helperFunc(root, root.val)
