# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeRecursive(root)

    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        self.invertTreeRecursive(root.left)
        self.invertTreeRecursive(root.right)

        left = root.left
        root.left = root.right
        root.right = left

        return root