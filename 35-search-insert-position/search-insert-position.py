from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # пока левая граница не пересекла правую
        while left <= right:
            # середина диапазона
            mid = (left + right) // 2
            
            # если нашли число — возвращаем индекс
            if nums[mid] == target:
                return mid
            
            # если target правее
            elif nums[mid] < target:
                left = mid + 1
            
            # если target левее
            else:
                right = mid - 1
        
        # если не нашли, left — позиция для вставки
        return left