# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        count = 1
        i = 0
        if current_node is None:
            return head
        while current_node.next is not None:
            count += 1
            current_node = current_node.next
        
        if count % 2 == 0:
            check_node = head
            while i != (count//2):
                check_node = check_node.next
                i += 1
            return check_node
        else:
            current_node = head
            while i != count//2:
                current_node = current_node.next
                i += 1
            return current_node
