from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # индекс последнего значимого элемента nums1
        p1 = m - 1
        
        # индекс последнего элемента nums2
        p2 = n - 1
        
        # индекс последней позиции в nums1
        p = m + n - 1
        
        # пока есть элементы в обоих массивах
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # если остались элементы в nums2 — копируем их
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
