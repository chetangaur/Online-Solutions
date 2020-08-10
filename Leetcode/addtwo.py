# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Parent = ListNode()
        last = Parent
        remain = 0 
        while l1 or  l2 or remain:
            tmp = ListNode()
            l1_val = 0 
            l2_val = 0 
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val

            value = remain + l2_val + l1_val
            if value >9 :
                value = value %10
                remain = 1
            else:
                remain = 0
            tmp.val = value
            last.next = tmp
            last = tmp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return Parent.next


