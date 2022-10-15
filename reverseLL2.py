# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0, head)
        left_previous = dummy
        for i in range(left-1):
            left_previous, current = current, current.next
        
        previous = None
        for i in range(right - left + 1):
            temp_next = current.next
            current.next = previous
            previous, current = current, temp_next
            
        left_previous.next.next = current
        left_previous.next = previous
        return dummy.nex
