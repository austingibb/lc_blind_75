# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        subRoot_hash = self.hashTree(subRoot)
        cache = set()
        self.hashTree(root, cache=cache)
        return subRoot_hash in cache

    def hashTree(self, root, cache=None):
        hl, hr = None, None
        if root.left:
            hl = self.hashTree(root.left, cache=cache)
        if root.right:
            hr = self.hashTree(root.right, cache=cache)

        roothash = hash(str(hash(root.val)) + str(hl) + str(hr))
        if cache is not None:
            cache.add(roothash)
        return roothash
        