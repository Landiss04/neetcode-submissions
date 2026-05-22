from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(0)   # needed so ans.next works
        curr = ans

        while list1 is not None and list2 is not None:
            temp1 = list1
            temp2 = list2
            nxt1 = temp1.next
            nxt2 = temp2.next

            if temp1.val < temp2.val:
                curr.next = temp1
                list1 = nxt1
            else:
                curr.next = temp2
                list2 = nxt2

            curr = curr.next  # advance pointer

        while list1 is not None:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2 is not None:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return ans.next