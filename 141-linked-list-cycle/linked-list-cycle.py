# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        if not head or not  head.next or not head.next.next:
            return False
        fast=head.next.next
        while fast and fast.next:
            if fast==slow:
                return True
            slow=slow.next
            fast=fast.next.next
        return False