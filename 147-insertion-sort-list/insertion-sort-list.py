# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        t=head
        while t:
            ls.append(t.val)
            t=t.next
        ls.sort()
        t=head
        for i in ls:
            t.val=i
            t=t.next
        return head