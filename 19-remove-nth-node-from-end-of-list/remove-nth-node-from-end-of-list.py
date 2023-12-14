# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=head
        r=head
        n+=1
        while n:
            if r:
                r=r.next
            else:
                return l.next
            n-=1
        while r:
            l=l.next
            r=r.next
        l.next=l.next.next
        return head