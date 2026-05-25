class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for index in range(len(nums)):
            hmap[nums[index]] = index

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in hmap and hmap[difference] != index:
                return [index, hmap[difference]]