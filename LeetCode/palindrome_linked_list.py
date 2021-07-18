# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        stk = list()
        slow = head
        while head:
            stk.append(head)
            head = head.next
        while stk:
            if slow.val != stk.pop().val:
                return False
            slow = slow.next
        return True