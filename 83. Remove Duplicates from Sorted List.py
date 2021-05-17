'''
Solving Theory
compare current and next, if next is equal current then delete next
If no equal to next, next will remain its number
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
       
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
        return head