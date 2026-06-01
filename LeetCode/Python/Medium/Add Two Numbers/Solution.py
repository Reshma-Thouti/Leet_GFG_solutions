# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        cs=0
        res=ListNode(0)
        ans=res
        while l1 or l2 or c:
            cs=l1.val if l1 else 0 
            cs+=l2.val if l2 else 0
            ans.next=ListNode((c+cs)%10)
            ans=ans.next
            c=(c+cs)//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return res.next