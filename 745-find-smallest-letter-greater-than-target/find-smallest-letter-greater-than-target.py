from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            # середина диапазона
            mid = (left + right) // 2
            
            # если mid буква <= target, ответ правее
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # left указывает на первую букву > target
        # если вышли за массив — берём первую (цикличность)
        return letters[left] if left < len(letters) else letters[0]
