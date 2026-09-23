# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0,head)
        prev , curr = dummy , head
        while curr and curr.next:
            nextPair = curr.next.next
            secondPair = curr.next

            secondPair.next = curr
            curr.next = nextPair
            prev.next = secondPair

            prev = curr
            curr = nextPair
        return dummy.next
        