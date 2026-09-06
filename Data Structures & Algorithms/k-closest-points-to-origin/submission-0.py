class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        output = []
        heapq.heapify(distances)

        for x, y in points:
            dist = (x)**2 + (y)**2
            heapq.heappush(distances, [dist, x, y])

        for _ in range(k):
            lower = heapq.heappop(distances)
            output.append([lower[1], lower[2]])

        return output

        