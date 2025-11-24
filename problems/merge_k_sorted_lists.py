from typing import Optional
from classes import ListNode

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        vals = []

        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                vals.append(curr.val)
                curr = curr.next
        
        vals.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in range(len(vals)):
            curr.next = ListNode(vals[val])
            curr = curr.next

        return dummy.next