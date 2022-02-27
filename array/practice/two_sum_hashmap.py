

from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int):
        prevMap = {}  # val:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
