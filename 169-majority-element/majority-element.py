class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]) is None:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        return max(dict,key=dict.get)