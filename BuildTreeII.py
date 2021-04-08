# 106. Construct Binary Tree from Inorder and Postorder Traversal
from typing import List
# For the following binary tree:
#         B
#       /  \
#      Z    S
#     / \  / \
#    H  J F   D
#
# in  : [H,Z,J,  B,  F,S,D]
# post: [H,J,Z,  F,D,S,  B]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) != len(postorder):
            return None
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root_val = postorder[-1]
        curr_node = TreeNode(root_val)

        for i in range(len(inorder)):
            if root_val == inorder[i]:
                left_size = i
                break

        inorder_left = inorder[: left_size]
        inorder_right = inorder[left_size+1:]
        postorder_left = postorder[: left_size]
        postorder_right = postorder[left_size:-1]

        curr_node.left = self.buildTree(inorder_left, postorder_left)
        curr_node.right = self.buildTree(inorder_right, postorder_right)

        return curr_node

# For the following binary tree:
#         1
#       /  \
#      2    3
#     / \  / \
#    4  5 6   7
# (a) Inorder (Left, Root, Right) : 4 2 5 1 6 3 7
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3 6 7
# (c) Postorder (Left, Right, Root) : 4 5 2 6 7 3 1

# Algorithm Inorder(tree)
#    1. Traverse the left subtree, i.e., call Inorder(left-subtree)
#    2. Visit the root.
#    3. Traverse the right subtree, i.e., call Inorder(right-subtree)

# Algorithm Preorder(tree)
#    1. Visit the root.
#    2. Traverse the left subtree, i.e., call Preorder(left-subtree)
#    3. Traverse the right subtree, i.e., call Preorder(right-subtree)

# Algorithm Postorder(tree)
#    1. Traverse the left subtree, i.e., call Postorder(left-subtree)
#    2. Traverse the right subtree, i.e., call Postorder(right-subtree)
#    3. Visit the root.
