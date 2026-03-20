# 1.Binary Tree
# it is a independent tree means it does not have any rules for tree structure and one parent has maximum 2 child

#2. Binary search Tree
# it contains the property of binary tree but the left sub tree always smaller than the right parent tree and right child tree is always greater than the parent 

#3. Strict/full Binary Tree
# Parent has 0 or 2 child

#4. Complete Binary Tree
# we can not putt element in right if left is vacant .....previous level should always full then we can go next level

# 5. Skew Binary Tree
#           1.Right Skewewd Tree
#           1.left Skewewd Tree
# ALL elements are in either left side or right side ....and there is only one element in each level

# 6. Extended  Binary Tree
# we extended the tree with dummy node

# Implementation (In Array)
# left child index={(index)*2+1}
# right child index={(index)*2+2}
# always go through left to right
# And it is only applicable for balance tree and make dummy node

# Implementation(LinkList):
# 