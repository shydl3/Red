'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k,
return the k closest points to the origin (0, 0).
'''
import heapq

class Solutions:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squared_dist(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -self.squared_dist(points[i])

            # If this point is closer than the kth farthest,
            # discard the farthest point and add this one
            # 相当于先用给定的前k个元素创建堆，再将剩余元素逐一比较，更新堆
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))

        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]

    def squared_dist(self, point: list[int]) -> int:
        return point[0]**2 + point[1]**2

'''
直接排序会造成O(n logn)复杂度，
如果维护k个元素的堆则仅需要O(n logk)复杂度
特别是当 k 远小于 n 时更快
'''