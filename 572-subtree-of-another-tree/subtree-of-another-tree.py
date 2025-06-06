# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (not p and not q) if (not p or not q) else (
            p.val == q.val
            and self.isSametree(p.left, q.left)
            and self.isSametree(p.right, q.right)
        )
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return False if not root else (
            self.isSametree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
