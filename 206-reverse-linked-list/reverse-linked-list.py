# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1    2     3    4    5
#            s    curr f

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # curr = head
        # prev= None
        # while curr is not None:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # return prev

        # recursive
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

