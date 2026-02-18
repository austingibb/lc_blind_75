from collections import deque
from typing import Optional, List, Any

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level_order(arr: List[Any]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order array representation where None means "no node".
    Example: [1,2,3,None,None,4,5]
    """
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        # left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        # right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root



class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q = deque()
        q.append((1, root))
        s = []
        while q:
            idx, node = q.popleft()
            s.append("{}:{}".format(idx, node.val))
            if node.left:
                q.append((2*idx, node.left))
            if node.right:
                q.append((2*idx+1, node.right))
        
        return " ".join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # base case if string is empty return None
        if data.strip() == "":
            return None

        # queue for each node calulate it's left and right child's index
        #   if index is in the tree create child, add its index and node to queue
        idx_to_val = {}
        for s in data.split(" "):
            s_split = s.split(":")
            idx = int(s_split[0])
            val = int(s_split[1])
            idx_to_val[idx] = val
        
        q = deque()
        root = TreeNode(idx_to_val[1])
        q.append((1, root))

        while q:
            idx, node = q.popleft()
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if left_idx in idx_to_val:
                left = TreeNode(idx_to_val[left_idx])
                node.left = left
                q.append((left_idx, left))
            
            if right_idx in idx_to_val:
                right = TreeNode(idx_to_val[right_idx])
                node.right = right
                q.append((right_idx, right))
        
        return root


def main():
    # Example input from prompt:
    root_arr = [1, 2, 3, None, None, 4, 5]

    # Build the tree from the input array
    root = build_tree_level_order(root_arr)

    codec = Codec()

    # Serialize
    serialized = codec.serialize(root)
    print("Serialized:", serialized)

    # Deserialize
    rebuilt = codec.deserialize(serialized)

    # Serialize again to verify round-trip
    serialized_again = codec.serialize(rebuilt)
    print("Serialized again:", serialized_again)

    print("Round-trip OK?", serialized == serialized_again)


if __name__ == "__main__":
    main()