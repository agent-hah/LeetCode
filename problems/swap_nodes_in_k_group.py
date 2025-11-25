from typing import Optional
from classes import ListNode

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    key = {}
    index = 0
    for i in range(k-1, len(vals), k):
        j = 0
        while j < k:
            key[index] = vals[i - j]
            index += 1
            j += 1

    dummy = ListNode(0)
    curr = dummy
    for i in range(len(vals)):
        if i in key:
            curr.next = ListNode(key[i])
        else:
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

res = reverseKGroup(example_1, 4)

prn = []
curr = res
while curr:
    prn.append(curr.val)
    curr = curr.next

print(prn)