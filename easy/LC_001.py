from typing import List


class Solution(object):
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:  # return type List<Integer>
        for i in range(len(nums)):  # loop till length of nums[]
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    print(two_sum([3, 2, 4], 6))
