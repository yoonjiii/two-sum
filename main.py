from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    for i in range(len(nums)):
        element = nums[i]
        j = i+1
        for num in nums[i+1:]:
            if element+num == target:
                print("Output: [" + str(i) + "," + str(j) + "]")
                return
            j += 1
    return