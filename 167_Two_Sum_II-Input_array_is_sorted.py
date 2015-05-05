# 2015-05-05  Runtime: 55 ms

class Solution:
    # @param {integer[]} numbers
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, numbers, target):
        smallIndex, bigIndex = 0, len(numbers) - 1
        while smallIndex < bigIndex:
            Sum = numbers[smallIndex] + numbers[bigIndex]
            if Sum == target: return [smallIndex + 1, bigIndex + 1]
            if Sum < target:
                smallIndex += 1
            else:
                bigIndex -= 1