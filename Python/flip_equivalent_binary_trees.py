# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        # If both nodes are None, they are equivalent
        if not root1 and not root2:
            return True
        # If one node is None but the other is not, they are not equivalent
        if not root1 or not root2:
            return False
        # If the values of the nodes are different, they are not equivalent
        if root1.val != root2.val:
            return False
        
        # Check if subtrees are equivalent without flipping or with flipping
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))