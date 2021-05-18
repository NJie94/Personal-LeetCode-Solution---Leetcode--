# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        list1, list2 = [], []
        prev,head = None, None
        sum = 0
        
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        
        while list1 or list2:
            sum = sum/10
            if list1:
                sum += list1.pop()
            if list2:
                sum += list2.pop()
            
            head = ListNode(sum%10)
            head.next = prev
            prev = head
        
        if sum >= 10:
            head = ListNode(sum/10)
            head.next = prev
            
        return head
        
    