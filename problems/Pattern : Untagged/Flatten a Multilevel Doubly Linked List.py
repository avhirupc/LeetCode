"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        def flattenUtil(head):
            ptr,prev=head,head
            while(ptr):
                if ptr.child:
                    ch,ct = flattenUtil(ptr.child)
                    ptr_next=ptr.next
                    ptr.next, ch.prev = ch, ptr
                    if ptr_next:
                        ptr_next.prev, ct.next = ct, ptr_next
                    ptr.child=None
                    prev=ptr
                    ptr=ptr_next
                else:
                    prev=ptr
                    ptr=ptr.next
            return head, prev
        head, tail = flattenUtil(head)
        return head
        