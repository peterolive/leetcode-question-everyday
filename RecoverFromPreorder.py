class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        from collections import defaultdict
        count = 1
        map_ = defaultdict(TreeNode)
        S = S.split('-')
        head = TreeNode(-1)
        map_[-1] = head
        prev_head = map_[-1]
        curr_head = TreeNode(S[0])
        map_[0] = curr_head
        prev_head.left = curr_head
        for i in range(1, len(S)):
            if S[i] == '':
                count += 1
            else:
                prev = map_[count - 1]
                curr = TreeNode(S[i])
                map_[count] = curr

                if prev.left:
                    prev.right = curr
                else:
                    prev.left = curr
                count = 1

        return head.left
