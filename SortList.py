class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None

        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)

        return self.merge(sorted_left, sorted_right)

    def find_middle(self, head):
        if not head or not head.next:
            return head
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(-1)
        curr_node = dummy

        while l1 and l2:
            if l1.val >= l2.val:
                curr_node.next = l2
                l2 = l2.next
            else:
                curr_node.next = l1.val
                l1 = l1.next
            curr_node = curr_node.next

        if l1:
            curr_node.next = l1
        if l2:
            curr_node.next = l2

        return dummy.next
