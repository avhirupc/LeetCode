# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return None
        #get the new head
        def get_min_node(lists):
            itr=0
            min_itr,min_value=-1,float("inf")
            end_reached_cntr=0
            #find min
            while(itr<len(lists)):
                if not lists[itr]:
                    end_reached_cntr+=1
                if lists[itr] and lists[itr].val < min_value:
                    min_value = lists[itr].val
                    min_itr=itr
                itr+=1
            end_flg = end_reached_cntr==len(lists)
            return end_flg,min_itr
            
        
        head=None
        end_flg, min_itr = get_min_node(lists)
        if min_itr==-1:
            return None
        
        head = lists[min_itr]
        ptr = head                         
        lists[min_itr]=lists[min_itr].next
        
        while(True):
            end_flg, min_itr = get_min_node(lists)
            if end_flg:
                break
            ptr.next=lists[min_itr]
            ptr=lists[min_itr]
            lists[min_itr]=lists[min_itr].next
            
        return head
    
    
            
            
        
        
        
