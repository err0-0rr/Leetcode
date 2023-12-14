# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        prt=head
        
        while list1 and list2:
            if list2.val<list1.val:
                prt.next=list2
                prt=list2
                list2=list2.next
            else:
                prt.next=list1
                prt=list1
                list1=list1.next
        
        if list1:
            prt.next=list1
        else:
            prt.next=list2
        return head.next