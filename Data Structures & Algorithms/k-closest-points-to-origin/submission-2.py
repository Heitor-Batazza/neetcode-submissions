class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        output = []
        

        for x, y in points:
            dist = (x)**2 + (y)**2
            distances.append([dist, x, y])

        heapq.heapify(distances)

        for _ in range(k):
            dist, x, y = heapq.heappop(distances)
            output.append([x, y])

        return output

        