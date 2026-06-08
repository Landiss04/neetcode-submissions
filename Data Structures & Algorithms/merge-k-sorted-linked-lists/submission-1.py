from typing import List, Optional

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(0)  # dummy head

        for i in range(len(lists)):
            curr1 = lists[i]

            while curr1:
                # find insertion point
                prev = ans
                while prev.next and prev.next.val < curr1.val:
                    prev = prev.next

                # insert node
                new_node = ListNode(curr1.val)
                new_node.next = prev.next
                prev.next = new_node

                curr1 = curr1.next

        return ans.next
