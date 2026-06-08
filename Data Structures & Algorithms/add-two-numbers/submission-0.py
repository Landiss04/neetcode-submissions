# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""

        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next

        s_i = int(s1) + int(s2)
        s = str(s_i)

        ans = ListNode(0)
        curr = ans

        for c in reversed(s):
            curr.next = ListNode(int(c))
            curr = curr.next

        return ans.next