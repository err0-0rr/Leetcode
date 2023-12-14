# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=[]
        large=[]
        count=0
        temp=head
        while temp!=None:
            if temp.val<x:
                small.append(temp.val)
            else:
                large.append(temp.val)
            temp=temp.next
        temp=head
        i=0
        j=0
        while temp!=None:
            if i<len(small):
                temp.val=small[i]
                i+=1
            else:
                temp.val=large[j]
                j+=1
            temp=temp.next
        return head