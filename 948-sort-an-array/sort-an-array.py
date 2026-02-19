from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # сортировка слиянием
        def merge_sort(arr):
            # базовый случай
            if len(arr) <= 1:
                return arr
            
            # делим массив
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # сливаем половины
            return merge(left, right)
        
        # слияние двух отсортированных массивов
        def merge(left, right):
            i = j = 0
            result = []
            
            # пока есть элементы в обоих массивах
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # добавляем остатки
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        return merge_sort(nums)
