"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            clone = Node(curr.val, curr.next)
            curr.next = clone
            curr = clone.next
        
        curr = head
        while curr:
            clone = curr.next
            clone.random = curr.random.next if curr.random else None
            curr = clone.next
        
        curr = head
        new_head = head.next
        while curr:
            clone = curr.next
            curr.next = clone.next 
            clone.next = clone.next.next if clone.next else None
            curr = curr.next
        return new_head
            
