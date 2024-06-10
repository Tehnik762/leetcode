# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made
# by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        state = ListNode()
        if list1 == None:
            if list2 == None:
                return None
            else:
                state.val = list2.val
                list2 = list2.next
                list1 = None
        elif list2 == None:
            state.val = list1.val
            list1 = list1.next
            list2 = None
        elif list1.val > list2.val:
            state.val = list2.val
            list2 = list2.next
        else:
            state.val = list1.val
            list1 = list1.next
        state.next = self.mergeTwoLists(list1, list2)
        return state
