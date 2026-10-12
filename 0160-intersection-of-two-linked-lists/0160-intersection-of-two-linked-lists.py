# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        if head1 is None or head2 is None:
            return None
        temp1=head1
        temp2=head2
        while temp1 != temp2:
            
            if temp1 is None:
                temp1 = head2
            else:
                temp1 = temp1.next

            if temp2 is None:
                temp2 = head1
            else:
                temp2 = temp2.next
        return temp1