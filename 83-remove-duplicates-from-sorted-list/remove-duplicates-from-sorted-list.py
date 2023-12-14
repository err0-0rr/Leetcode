# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        while ptr!=None and ptr.next!=None:
            if ptr.next.val==ptr.val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head