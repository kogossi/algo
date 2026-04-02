class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)  # сначала корень
            
            if node.right:
                stack.append(node.right)  # потом правый
            if node.left:
                stack.append(node.left)   # потом левый
        
        return res