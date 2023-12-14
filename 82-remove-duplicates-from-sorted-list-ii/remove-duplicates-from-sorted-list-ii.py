# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Replace items starting from first node and replce the value wiith unique value
        temp=head
        cur=None
        while temp!=None:
            val=temp.val
            count=1
            while temp.next!=None and temp.next.val==val:
                count+=1
                temp=temp.next
            if count==1:
                if not cur:
                    cur=head
                else:
                    cur=cur.next
                cur.val=val
            temp=temp.next
        if not cur:
            return cur
        cur.next=None
        return head