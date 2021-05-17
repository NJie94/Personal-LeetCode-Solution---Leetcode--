# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        solve1, solve2 = temp, temp
        
        while solve2:
            if(n<= -1):
                solve1 = solve1.next
            solve2 = solve2.next
            n-=1
        
        solve1.next = solve1.next.next
        return temp.next
        