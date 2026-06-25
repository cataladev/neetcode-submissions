class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} #val:index
        for i in range(len(nums)):
            if(target - nums[i] in Map):
                return[Map[target-nums[i]], i]
            else:
                Map.update({nums[i]: i})
        return 