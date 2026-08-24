# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def f(temp):
            if temp == None or temp.next == None:
                return temp
            curnext = temp.next
            temp.next = curnext.next
            print(curnext.val)
            curnext.next = temp
            temp.next = f(temp.next)
            
            return curnext
        
        head = f(temp)
        return head
