class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_head = even
        while(odd is not None and odd.next is not None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head