# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # ✅ Step 1: find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        mid = length // 2

        # ✅ Step 2: split into two lists
        hi = ListNode(0)
        lo = ListNode(0)
        curr1 = hi
        curr2 = lo

        curr = head
        count = 0

        while curr:
            if count >= mid:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next

            count += 1
            curr = curr.next

        # ✅ Step 3: reverse second half
        hi = self.reverse(hi.next)

        # ✅ Step 4: merge alternately
        ans = ListNode(0)
        curr = ans

        curr1 = lo.next
        curr2 = hi
        count = 0

        while curr1 or curr2:
            if count % 2 == 0 and curr1:
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            elif curr2:
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next

            curr = curr.next
            count += 1

        # ✅ Step 5: copy values back into original list
        curr = head
        new_curr = ans.next
        while curr and new_curr:
            curr.val = new_curr.val
            curr = curr.next
            new_curr = new_curr.next

        return

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
