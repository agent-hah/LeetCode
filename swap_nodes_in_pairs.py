from typing import Optional
from classes import ListNode

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    for i in range(1, len(vals), 2):
        val1 = vals[i]
        val2 = vals[i - 1]
        vals[i - 1] = val1
        vals[i] = val2

    dummy = ListNode(0)
    curr = dummy
    for i in range(len(vals)):
        curr.next = ListNode(vals[i])
        curr = curr.next

    return dummy.next


example_1 = ListNode(1)

part2 = ListNode(2)
example_1.next = part2
part3 = ListNode(3)
part2.next = part3
part4 = ListNode(4)
part3.next = part4
part5 = ListNode(5)
part4.next = part5

res = swapPairs(example_1)

prn = []
curr = res
while curr:
    prn.append(curr.val)
    curr = curr.next

print(prn)