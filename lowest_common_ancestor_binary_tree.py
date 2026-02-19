# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []
        q_path = []

        self.find_node_path(root, p, p_path)
        self.find_node_path(root, q, q_path)

        # print("p_path", " -> ".join(map(lambda node: str(node.val), p_path)))
        # print("q_path", " -> ".join(map(lambda node: str(node.val), q_path)))

        shortest_length = min(len(p_path), len(q_path))
        for i in range(0, shortest_length):
            if p_path[i] != q_path[i]:
                return p_path[i-1]

        return p_path[shortest_length-1]

        
    def find_node_path(self, root, n, path):
        cur = root
        path.append(root)
        while cur.val != n.val and (cur.left or cur.right):
            if n.val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    return []
            elif n.val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    return []
            
            path.append(cur)
