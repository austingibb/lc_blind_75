# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        return self.merge_k_lists_divide(lists)
    
    def merge_k_lists_divide(self, lists):
        if not lists:
            return None

        lists = filter(lambda l: l is not None, lists)
        if len(lists) == 0:
            return None

        return self.merge_k_lists_recurse(0, len(lists)-1, lists)

    def merge_k_lists_recurse(self, i, j, lists):
        if i == j:
            return lists[i]

        mid = (i + j)//2

        left = self.merge_k_lists_recurse(i, mid, lists)
        right = self.merge_k_lists_recurse(mid+1, j, lists)

        prev = None
        head = None
        while left is not None or right is not None:
            min_node = None
            if left is None:
                min_node = right
                right = right.next
            elif right is None:
                min_node = left
                left = left.next
            elif left.val < right.val:
                min_node = left
                left = left.next
            else:
                min_node = right
                right = right.next
            
            if not head:
                head = min_node

            if prev is not None:
                prev.next = min_node

            prev = min_node

        return head

    def merge_k_lists_naive(self, lists):
        head = None
        prev = None

        while True:
            min_node_idx = -1
            min_node = None
            for i, node in enumerate(lists):
                if node and (min_node is None or node.val < min_node.val):
                    min_node = node
                    min_node_idx = i

            if min_node is None:
                break

            if not head:
                head = min_node

            if prev:
                prev.next = min_node

            lists[min_node_idx] = min_node.next

            prev = min_node
        
        return head