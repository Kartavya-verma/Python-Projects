# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # if not head:
        #     return None
        #
        # lastElement = head
        # length = 1
        # while (lastElement.next):
        #     lastElement = lastElement.next
        #     length += 1
        #
        # lastElement.next = head
        # k = k % length
        # tempNode = head
        # for _ in range(length - k - 1):
        #     tempNode = tempNode.next
        #
        #
        # answer = tempNode.next
        # tempNode.next = None
        #
        # return answer


        if not head :
            return  None

        length = 1
        last = head
        while last.next:
            length += 1
            last = last.next

        k %= length
        last.next = head

        temp = head
        for _ in range(length-k-1):
            temp = temp.next

        ans = temp.next
        temp.next = None


































