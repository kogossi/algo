import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        
        # массив для отслеживания посещённых вершин
        visited = [False] * n
        
        # минимальная куча (вес, вершина)
        min_heap = [(0, 0)]
        
        result = 0
        edges_used = 0

        while edges_used < n:
            cost, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            # отмечаем вершину как посещённую
            visited[u] = True
            result += cost
            edges_used += 1

            # добавляем все рёбра из текущей вершины
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))

        return result
