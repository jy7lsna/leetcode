# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_to_max_depth = {None: 0}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.populateMaxDepth(root)
        if not root:
            return 0
        
        # case1 : go thru the root
        left_max_depth = self.node_to_max_depth[root.left]
        right_max_depth = self.node_to_max_depth[root.right]
        case1 = left_max_depth + right_max_depth
        # case2: only consider left
        case2 = self.diameterOfBinaryTree(root.left)
        # case3 only right
        case3 = self.diameterOfBinaryTree(root.right)

        return max(case1, case2, case3)

    def populateMaxDepth(self, root):
        if root in self.node_to_max_depth:
            return
        
        self.populateMaxDepth(root.left)
        self.populateMaxDepth(root.right)

        self.node_to_max_depth[root] = 1 + max(
            self.node_to_max_depth[root.left],
            self.node_to_max_depth[root.right],
        )

