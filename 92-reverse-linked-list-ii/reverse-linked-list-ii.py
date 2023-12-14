# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ls=[]
        i=1
        temp=head
        ptr=head
        while temp!=None:
            if i>=left and i<=right:
                if i==left:
                    ptr=temp
                ls.insert(0, temp.val)
            i+=1
            temp=temp.next
        for i in ls:
            ptr.val=i
            ptr=ptr.next
        return head