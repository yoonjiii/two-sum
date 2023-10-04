from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        element = nums[i]
        j = i+1
        for num in nums[i+1:]:
            if element+num == target:
                return [i, j]
            j += 1
    return