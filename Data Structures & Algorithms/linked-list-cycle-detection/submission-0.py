from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        freq = {}

        while head is not None:
            temp = head
            nxt = head.next 

            if temp.val in freq and not freq[temp.val] <= 1:
                return True
            else:
                freq[temp.val] = freq.get(temp.val, 0) + 1

            head = nxt

        return False