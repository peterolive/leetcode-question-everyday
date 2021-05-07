class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        mid = self.find_middle(head)

        dummy_l, dummy_m, dummy_r = ListNode(-1), ListNode(-1), ListNode(-1)

        tail_l, tail_m, tail_r = dummy_l, dummy_m, dummy_r

        while head:
            if head.val < mid.val:
                tail_l.next = head
                tail_l = tail_l.next
            elif head.val > mid.val:
                tail_r.next = head
                tail_r = tail_r.next
            else:
                tail_m.next = head
                tail_m = tail_m.next
            head = head.next

        tail_l.next = None
        tail_m.next = None
        tail_r.next = None

        sorted_left = self.sortList(dummy_l.next)
        sorted_right = self.sortList(dummy_r.next)

        return self.connect(sorted_left, dummy_m.next, sorted_right)

    def find_middle(self, head):
        if not head or not head.next:
            return head

        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def connect(self, sorted_left, middle, sorted_right):
        dummy = ListNode(-1)
        curr_node = dummy

        while sorted_left:
            curr_node.next = sorted_left
            sorted_left = sorted_left.next
            curr_node = curr_node.next

        while middle:
            curr_node.next = middle
            middle = middle.next
            curr_node = curr_node.next

        curr_node.next = sorted_right

        return dummy.next
