import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # берем первые k элементов
        heap = nums[:k]
        
        # превращаем их в минимальную кучу
        heapq.heapify(heap)
        
        # смотрим остальные числа в массиве
        for num in nums[k:]:
            # если текущее число больше самого маленького вкуче
            if num > heap[0]:
                # заменяем минимальный элемент на новое число
                heapq.heappushpop(heap, num)
        
        # в корне кучи лежит k-й по величине элемент
        return heap[0]