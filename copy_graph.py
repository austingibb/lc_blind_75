class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque 

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]


def build_graph(adj: List[List[int]]) -> Optional[Node]:
    """
    Builds a graph from LeetCode's adjacency list representation.
    adj[i] contains the neighbors' values for node (i+1).
    Returns the Node for value 1, or None if adj is empty.
    """
    if not adj:
        return None

    # 1) Create all nodes
    nodes = {i + 1: Node(i + 1) for i in range(len(adj))}

    # 2) Wire up neighbors
    for i, neigh_vals in enumerate(adj, start=1):
        nodes[i].neighbors = [nodes[v] for v in neigh_vals]

    return nodes[1]

def main():
    # ---- Example usage ----
    adj = [[2,4],[1,3],[2,4],[1,3]]
    start = build_graph(adj)
    s = Solution()
    clone = s.cloneGraph(start)
    print(clone.val)
    print(clone.neighbors)

if __name__ == "__main__":
    main()