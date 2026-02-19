from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left — начало диапазона, right — конец
        left, right = 0, len(nums) - 1
        
        # пока границы не пересеклись
        while left <= right:
            # середина диапазона
            mid = (left + right) // 2
            
            # если нашли элемент
            if nums[mid] == target:
                return mid
            
            # если target правее середины
            elif nums[mid] < target:
                left = mid + 1
            
            # если левее середины
            else:
                right = mid - 1
        
        # если не нашли
        return -1