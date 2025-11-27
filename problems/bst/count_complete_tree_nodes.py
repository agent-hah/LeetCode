from typing import Optional
from classes import TreeNode

def countNodes(root: Optional[TreeNode]) -> int:
    def get_depth(root):
        num = 0
        while root:
            num += 1
            root = root.left
        return num
    if not root:
        return 0
    
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)

    if (left_depth == right_depth):
        return (1 << right_depth) + countNodes(root.right)
    else:
        return (1 << right_depth) + countNodes(root.left)

def countNodes2(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + countNodes2(root.left) + countNodes2(root.right)
    
root = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(4),
        TreeNode(5)
    ),
    TreeNode(
        3,
        TreeNode(6)
    )
)

print(countNodes(root))
print(countNodes2(root))