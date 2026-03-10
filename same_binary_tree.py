# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None or q is None:
            return p is None and q is None

        return self.same_tree_dfs(p, q)
        
    def same_tree_dfs(self, p, q):
        if p.val != q.val:
            return False

        left_same = False
        if ((p.left is not None) ^ (q.left is not None)):
            return False
        if p.left:
            left_same = self.same_tree_dfs(p.left, q.left)
        else:
            left_same = True 

        if not left_same:
            return False

        right_same = False
        if((p.right is not None) ^ (q.right is not None)):
            return False
        if p.right:
            right_same = self.same_tree_dfs(p.right, q.right)
        else:
            right_same = True
        
        return right_same
