class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stk=[]
        temp_ptr=head
        while(temp_ptr):
            stk.append(temp_ptr)
            temp_ptr=temp_ptr.next
        if len(stk)==0:
            return head
        node=stk.pop()
        head=node
        prev=node
        while(stk):
            node=stk.pop()
            prev.next=node
            prev=node
        prev.next=None
        
        return head
        