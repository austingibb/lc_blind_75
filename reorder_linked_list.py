# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next

        l = 0
        r = len(nodes)-1
        prev = None
        while l <= r:
            l_node, r_node = nodes[l], nodes[r]
            if prev:
                prev.next = l_node
            if l < r:
                l_node.next = r_node
            
            l += 1
            r -= 1
            prev = r_node
        
        prev.next = None

        return nodes[0]
