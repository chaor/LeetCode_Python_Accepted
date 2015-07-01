# 2015-06-30  Runtime: 144 ms
from heapq import *

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        LRH = [{'L':i[0], 'R':i[1], 'H':i[2]} for i in buildings]
        skyline, i, n = [], 0, len(LRH)
        maxHeap = [] # heappush, heappop is for min heap, so we store negative number
        while i < n or maxHeap:
            if not maxHeap or i < n and LRH[i]['L'] <= -maxHeap[0]['R']:
                x = LRH[i]['L']
                while i < n and LRH[i]['L'] == x:
                    heappush(maxHeap, {'H':-LRH[i]['H'], 'R':-LRH[i]['R']})
                    i += 1
            else:
                x = -maxHeap[0]['R']
                while maxHeap and -maxHeap[0]['R'] <= x:
                    heappop(maxHeap)
            height = -maxHeap[0]['H'] if len(maxHeap) > 0 else 0
            if not skyline or height != skyline[-1]['H']:
                skyline.append({'X':x, 'H':height})
        return [[i['X'], i['H']] for i in skyline]