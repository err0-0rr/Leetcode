# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr=head
        def reverse(ls, n):
            for i in range(n//2):
                temp=ls[i].val
                ls[i].val=ls[n-i-1].val
                ls[n-i-1].val=temp
        
        while True:
            flag=False
            ls=[]
            for i in range(k):
                if ptr==None:
                    flag=True
                    break
                else:
                    ls.append(ptr)
                ptr=ptr.next
            if flag:
                break
            else:
                reverse(ls, k)
        
        return head
                    