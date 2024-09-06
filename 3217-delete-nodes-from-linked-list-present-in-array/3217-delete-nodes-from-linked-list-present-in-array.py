# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        # Create a set from the list of numbers
        num_set = set(nums)
        
        # Handle the edge case where the list is empty
        if head is None:
            return None
        
        # Skip initial nodes that are in num_set
        temp = head
        while temp and temp.next and temp.val in num_set:
            temp = temp.next
        
        # The new head of the list after skipping initial nodes
        head = temp
        
        # Remove nodes that are in num_set from the remaining list
        while temp and temp.next:
            if temp.next.val in num_set:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
