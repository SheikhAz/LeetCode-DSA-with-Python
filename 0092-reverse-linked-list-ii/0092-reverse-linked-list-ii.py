# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0,head)
        prevL = dummy
        temp = head
        for i in range(left - 1):
            prevL = temp
            temp = temp.next
        prev = None
        for i in range(right - left + 1):
            tempNxt = temp.next
            temp.next = prev
            prev = temp
            temp = tempNxt
        prevL.next.next = temp
        prevL.next = prev
        return dummy.next