class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)  # корень
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]  # переворачиваем (left-right-root)