# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListIterative(head)
        return self.reverseListRec(head, None)
    
    def reverseListRec(self, curr: Optional[ListNode], prev:Optional[ListNode]) -> Optional[ListNode]:
        next_node = curr.next
        curr.next = prev
        return self.reverseListRec(next_node, prev)

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            
            prev = curr
            curr = next_node
        return prev

