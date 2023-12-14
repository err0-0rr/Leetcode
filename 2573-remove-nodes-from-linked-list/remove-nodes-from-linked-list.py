# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        t=head
        while t:
            while ls and t.val>ls[-1].val:
                ls.pop()
            ls.append(t)
            t=t.next
        
        for i in range(len(ls)-1):
            ls[i].next=ls[i+1]
        return ls[0]