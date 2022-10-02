# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        current = head
        while current !=None:
            store.append(current.val)
            current = current.next
        store = sorted(set(store))
        head = ListNode()
        new_head = head
        for x in store:
            add = ListNode(x)
            new_head.next = add
            new_head = new_head.next
        return head.next
