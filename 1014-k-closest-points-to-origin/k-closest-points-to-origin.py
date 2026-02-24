class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        # считаем расстояние до (0,0) для каждой точки
        for x, y in points:
            dist = x*x + y*y   # берем квадрат расстояния, корень не нужен
            
            # кладем в кучу пару (расстояние, точка)
            heapq.heappush(heap, (dist, [x, y]))
        
        result = []
        
        # достаем k точек с минимальным расстоянием
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result