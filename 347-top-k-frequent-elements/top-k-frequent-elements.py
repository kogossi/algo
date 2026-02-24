class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # считаем сколько раз встречается каждое число
        count = Counter(nums)
        
        # создаем список "карманов" по частоте
        # индекс = сколько раз встречается число
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # раскладываем числа по карманам
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        
        # идем с конца, т.к. там самые частые элементы
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                
                # как только набрали k элементов — возвращаем ответ
                if len(result) == k:
                    return result