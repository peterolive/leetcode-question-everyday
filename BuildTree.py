# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# For the following binary tree:
#         B
#       /  \
#      Z    S
#     / \  / \
#    H  J F   D
#
# pre : [B,  Z,H,J,  S,F,D]
# in  : [H,Z,J,  B,  F,S,D]
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder):
            return None
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_val = preorder[0]
        curr_node = TreeNode(root_val)

        for i in range(len(inorder)):
            if root_val == inorder[i]:
                left_size = i
                break

        preorder_left = preorder[1: left_size + 1]
        preorder_right = preorder[left_size+1:]
        inorder_left = inorder[:left_size]
        inorder_right = inorder[left_size+1:]

        curr_node.left = self.buildTree(preorder_left, inorder_left)
        curr_node.right = self.buildTree(preorder_right, inorder_right)

        return curr_node
