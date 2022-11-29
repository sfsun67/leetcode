'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from math import ceil


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def middleNode(self, head):
        #l = ListNode()
        h=0
        while head.next:
            h += 1
        half_h = (h+1)/2-1
        #outlist = list()
        if type(half_h) == int:
            outlist = head[half_h:]
            return(outlist)
        else:
            half_h = ceil(half_h)
            outlist = head[half_h:]
            return(outlist)

        


s = Solution()
head = [1,2,3,4,5,6,7,8]
print(s.middleNode(head))