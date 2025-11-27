from typing import Optional
from classes import *

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return None
    res = head

    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    target = length - n

    if target == 0:
        return res.next

    def recursion (res, prev: Optional[ListNode], curr: Optional[ListNode], ticker: int) -> None:
        if not curr:
            return

        if ticker == target:
            if not prev:
                res = curr.next
                return
            
            prev.next = curr.next
            return
        
        recursion(res, curr, curr.next, ticker + 1)
    
    recursion(res, None, head, 0)
    return res

example_1 = ListNode(1)

part2 = ListNode(2)
example_1.next = part2
part3 = ListNode(3)
part2.next = part3
part4 = ListNode(4)
part3.next = part4
part5 = ListNode(5)
part4.next = part5

res = removeNthFromEnd(example_1, 2)

prn = []
curr = res
while curr:
    prn.append(curr.val)
    curr = curr.next

print(prn)