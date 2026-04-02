class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)  # идем влево
                root = root.left
            
            root = stack.pop()
            res.append(root.val)  # добавили корень
            root = root.right     # теперь вправо
        
        return res