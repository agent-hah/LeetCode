from classes import *

def mergeTwoLists(list1, list2):
    l1 = []
    l2 = []
    while (list1):
        l1.append(list1.val)
        list1 = list1.next
    while (list2):
        l2.append(list2.val)
        list2 = list2.next
    result = sorted(l1 + l2)
    dummy = ListNode(0)
    curr = dummy
    for i in range(len(result)):
        curr.next = ListNode(result[i])
        curr = curr.next
    return dummy.next

dummy = ListNode(0)
curr = dummy
for i in range(30):
    curr.next = ListNode(i)
    curr = curr.next

n = mergeTwoLists(dummy.next, dummy.next)

result = []
while (n):
    result.append(n.val)
    n = n.next

print(result)