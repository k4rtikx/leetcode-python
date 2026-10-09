# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        fast =head 
        slow=head
        if head is None:
            return head
        for i in range(n):
            fast=fast.next

        if fast is None:
            head = head.next
            return head #n equals the list length,
        
        while fast.next is not None :
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head