# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=0
        temp=head
        last=None
        while temp!=None:
            l+=1
            if temp.next==None:
                last=temp
            temp=temp.next
        if l==0 or l==1:
            return head
        k=k%l
        if k==0:
            return head
        init_head=head
        temp=head
        count=l-k-1
        while count>0:
            temp=temp.next
            count-=1
        head=temp.next
        temp.next=None
        last.next=init_head
        return head