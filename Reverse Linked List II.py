
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if head is None or head.next is None:
            return head

        if left == right:
            return head

        root2 = None
        roottemp = None
        postion = 1

        temp = head

        before = None

        while temp:

            if postion == left:
                before = temp
                break

            temp = temp.next
            postion += 1

        # Create reversed linked list
        count = left

        while temp and count <= right:
            root2 = ListNode(temp.val, root2)
            temp = temp.next
            count += 1

        # root2 is the head of reversed list
        roottemp = root2

        # Find the last node of reversed list
        last = roottemp

        while last.next:
            last = last.next

        # Connect reversed list with remaining nodes
        last.next = temp

        # Connect reversed list with previous nodes
        if left == 1:
            return root2

        postion = 1
        prev = head

        while postion < left - 1:
            prev = prev.next
            postion += 1

        prev.next = root2

        return head
