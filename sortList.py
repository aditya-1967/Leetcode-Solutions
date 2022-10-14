# 148. Sort List
# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        current_node = head
        while current_node != None:
            store.append(current_node.val)
            current_node = current_node.next
        store.sort()
        
        head = ListNode()
        new_head = head
        for x in store:
            add = ListNode(x)
            new_head.next = add
            new_head = new_head.next
        return head.next
