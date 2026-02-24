class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # делаем "максимальную" кучу через отрицательные числа
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # пока есть хотя бы два камня
        while len(max_heap) > 1:
            
            # берем два самых тяжелых
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            # если они не равны, возвращаем разницу обратно
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        # если камень остался — вернуть его, иначе 0
        return -max_heap[0] if max_heap else 0