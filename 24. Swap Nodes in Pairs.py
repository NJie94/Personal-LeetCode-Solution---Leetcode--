# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        temp = ListNode(0)
        temp.next = head
        curr = temp
        
        while curr.next and curr.next.next:
            next_x1 = curr.next
            next_x2 = curr.next.next
            next_x3 = curr.next.next.next
            
            curr.next = next_x2
            next_x2.next = next_x1
            next_x1.next = next_x3
            curr = next_x1
        return temp.next
            