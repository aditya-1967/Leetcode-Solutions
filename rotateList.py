# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        length = 0
        tail = head
        while tail.next != None:
            length += 1
            tail = tail.next
        length += 1
        tail.next = head
        rotate = length - k % length
        tail = head
        while rotate > 1:
            tail = tail.next
            rotate -= 1
        head = tail.next
        tail.next = None
        
        return head
