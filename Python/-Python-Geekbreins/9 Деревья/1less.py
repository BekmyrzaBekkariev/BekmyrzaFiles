# Cперва нужно скачать из cmd
# дерево
# pip install binarytree
# ---------------------------------------
# tree
# a = tree(height=4, is_perfect=False)
# print(a)

#              ___________23________
#             /                     \
#         ___6_____               ___8_______
#        /         \             /           \
#      _10         _11         _7           __21___
#     /   \       /   \       /  \         /       \
#   _25    0     26    22    13   14     _9
# ---------------------------------------

# bst
# b = bst(height=3, is_perfect=True)
# print(b)
#         ______7_______
#        /              \
#     __3__           ___11___
#    /     \         /        \
#   1       5       9         _13
#  / \     / \     / \       /   \
# 0   2   4   6   8   10    12    14

from binarytree import tree, bst, Node, build


class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)

b = bst(height=3, is_perfect=True)
print(b)

# Ручное дерево
# Node
# #    __7__
#    /     \
#   3       11
#  / \     /  \
# 1   5   9    13

c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)

# build создания дерево с помощью списка
#     __7__
#    /     \
#   3       11
#  / \     /  \
# 1   5   9    13
d = build([7, 3, 11, 1, 5, 9, 3])
