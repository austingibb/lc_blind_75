# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        nth_back_node = head
        prev_nth_back_node = None

        for i in range(0, n-1):
            current_node = current_node.next

        while current_node.next:
            current_node = current_node.next
            prev_nth_back_node = nth_back_node
            nth_back_node = nth_back_node.next

        if prev_nth_back_node:
            prev_nth_back_node.next = nth_back_node.next
        else:
            head = nth_back_node.next
            
        return head