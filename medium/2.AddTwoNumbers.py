# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number
# 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_n = str(l1.val)
        l2_n = str(l2.val)
        while l1.next != None:
            l1 = l1.next
            l1_n += str(l1.val)

        while l2.next != None:
            l2 = l2.next
            l2_n += str(l2.val)

        l1_n = l1_n[::-1]
        l2_n = l2_n[::-1]
        res = int(l1_n)+int(l2_n)
        res = str(res)
        t = None
        for l in res:
            t = ListNode(int(l), t)
        return t


