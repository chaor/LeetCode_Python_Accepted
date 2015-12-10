# 2015-12-09  83 tests, 1616 ms
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if not primes:
            return 1
        result, k = [1], len(primes)
        p, min_heap = [0] * k, [(primes[i], i) for i in range(k)]
        heapq.heapify(min_heap)
        for i in range(1, n):
            while min_heap[0][0] <= result[-1]:
                val, j = heapq.heappop(min_heap)
                p[j] += 1
                heapq.heappush(min_heap, (result[p[j]] * primes[j], j))
            val, j = heapq.heappop(min_heap)
            result.append(val)
            p[j] += 1
            heapq.heappush(min_heap, (result[p[j]] * primes[j], j))
        return result[n - 1]