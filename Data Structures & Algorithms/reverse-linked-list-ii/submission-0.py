# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev = dummy

        # Advance to node just before position 'left'
        for _ in range(left - 1):
            leftPrev = leftPrev.next
        curr = leftPrev.next        # First node to reverse

        # Reverse right - left nodes via head insertion
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt. next       # detach nxt from sequence
            nxt.next = leftPrev.next    # nxt goes to front of sublist
            leftPrev.next = nxt         # leftPrev now points to nxt
        return dummy.next