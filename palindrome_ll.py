# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        store = []
        current_node = head
        store.append(current_node.val)
        while current_node.next is not None:
            current_node = current_node.next
            store.append(current_node.val)
        if store == store[::-1]:
            return True
