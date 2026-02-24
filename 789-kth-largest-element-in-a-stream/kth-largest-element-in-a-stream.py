class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        # сохраняем числа
        self.heap = nums
        
        # делаем из списка минимальную кучу
        heapq.heapify(self.heap)

        # если чисел больше чем k, убираем самые маленькие
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # добавляем новое число в кучу
        heapq.heappush(self.heap, val)

        # если элементов стало больше k, удаляем минимальный
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # самый маленький в куче = k-й по величине в потоке
        return self.heap[0]