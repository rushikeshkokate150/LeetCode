# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        
        if head == None:
            return None
        if head.next ==  None:
            return head

        small = ListNode()
        smalltemp = small
        high = ListNode()
        hightemp = high

        temp = head


        while temp:
            if temp.val < x:
                smalltemp.next = ListNode(temp.val)
                smalltemp = smalltemp.next
            else:
                hightemp.next = ListNode(temp.val)
                hightemp = hightemp.next

            temp = temp.next
        
        if small.next == None:
            head = high.next
            return head

        head = small.next
        smalltemp.next = high.next
        
        return head