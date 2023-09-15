'''
Remove Nth node from the end of the list

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

'''

# Python3 Code

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        count = 1
        while ptr.next is not None:
            count += 1
            ptr = ptr.next
        ptr = head
        h = head
        c = 1
        p = ptr
        if n == count:
            h = h.next
            return h
        while c != count-n+1 and ptr is not None  and p.next is not None:
            c += 1
            p = ptr
            ptr = ptr.next

        if ptr.next == None:
            p.next = None
            return h
        elif ptr.next is not None:
            p.next = ptr.next
            return h

        

       