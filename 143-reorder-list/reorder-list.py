# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ls=[]
        prt=head
        while prt:
            ls.append(prt.val)
            prt=prt.next
        
        j=len(ls)-1
        i=0
        prt=head
        flag=True
        while prt:
            if flag:
                prt.val=ls[i]
                i+=1
            else:
                prt.val=ls[j]
                j-=1
            flag=not flag
            prt=prt.next
        
        