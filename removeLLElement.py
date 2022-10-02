# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        store = []
        current = head
        while current !=None:
            store.append(current.val)
            current = current.next
        
        store = list(filter((val).__ne__, store))
        head = ListNode()
        new_head = head
        for x in store:
            add = ListNode(x)
            new_head.next = add
            new_head = new_head.next
        return head.next
