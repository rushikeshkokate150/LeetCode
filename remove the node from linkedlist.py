# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp =head
        if temp.next == None:
            return head
        
        if temp.next.next == None:
            if temp.val >= temp.next.val:
                return head
            else:
                prev = temp
                temp = temp.next
                temp.next = prev
                prev.next = None
                head = temp
                return head


        def rev(head):
            prev = None
            temp = head
            curr = temp.next

            while curr:
                temp.next = prev
                prev = temp
                temp = curr
                curr = curr.next
            temp.next = prev
            return temp
        
        head = rev(temp)
        
        cur = head
        temp = head.next

        while temp:
            if temp.val < cur.val:
                temp = temp.next
            else:
                cur.next = temp
                cur = temp
                temp = temp.next
        
        cur.next = temp

        temp = head
        head = rev(temp)
        
        return head

