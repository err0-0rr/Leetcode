# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=None
        prt=head
        while prt!=None:
            next1=prt.next
            prt.next=temp
            temp=prt
            prt=next1
            
        return temp