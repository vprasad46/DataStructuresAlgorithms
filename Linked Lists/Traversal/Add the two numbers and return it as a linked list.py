# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        sum = l1.val + l2.val + c
        c = sum // 10
        self.l3 = ListNode(sum % 10)
        if l1.next != None and l2.next != None:
            self.l3.next = Solution().addTwoNumbers(l1.next, l2.next, c)
        else:
            return self.l3
        return self.l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val),
    result = result.next
# 7 0 8
