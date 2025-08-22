# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, key=0, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
        
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node