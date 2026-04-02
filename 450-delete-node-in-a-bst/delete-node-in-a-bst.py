class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # ищем слева
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)  # ищем справа
        else:
            if not root.left:
                return root.right  # один ребенок или нет
            if not root.right:
                return root.left
            
            # ищем минимум справа
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            root.val = min_node.val  # заменили
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root