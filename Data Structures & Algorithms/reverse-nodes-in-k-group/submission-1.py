from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count length
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        if n < k or head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while n >= k:
            prev = None
            curr = group_prev.next
            tail = curr  # will become the tail after reversal

            count = 0
            while count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1

            # reconnect group
            group_prev.next = prev
            tail.next = curr

            # move to next group
            group_prev = tail
            n -= k

        return dummy.next