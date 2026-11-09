# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k=len(lists)
        if k==0:
            return None
        if k==1 :
            if lists[0]==None:
                return None
            return lists[0]
        def merge(left, right):
            dummy = ListNode(-1)
            temp = dummy
            t1 = left
            t2 = right

            while t1 and t2:
                if t1.val < t2.val:
                    temp.next = t1
                    temp = temp.next
                    t1 = t1.next
                else:
                    temp.next = t2
                    temp = temp.next
                    t2 = t2.next
            
            while t1:
                temp.next = t1
                temp = temp.next
                t1 = t1.next

            while t2:
                temp.next = t2
                temp = temp.next
                t2 = t2.next
            
            return dummy.next
        
        def divide(l,r):
            if l == r:
                return lists[l]
            mid = (l+r)//2
            lf = divide(l,mid)
            rt = divide(mid+1,r)

            return merge(lf,rt)
        
        return divide(0,len(lists)-1)