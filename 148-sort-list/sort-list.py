# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        ls=[]
        
        while temp!=None:
            ls.append(temp.val)
            temp=temp.next
        
        ls.sort()
        i=0
        temp=head
        while temp!=None:
            temp.val=ls[i]
            i+=1
            temp=temp.next

        return head