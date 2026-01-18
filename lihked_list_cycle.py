# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hasCycleTwoPointer(head)

    def hasCycleHashmap(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()
        node = head
        while node:
            node_id = id(node)
            if node_id in seen:
                return True
            seen.add(node_id)
            node = node.next
        
        return False

    def hasCycleTwoPointer(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False