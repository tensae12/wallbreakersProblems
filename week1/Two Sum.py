class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, num in enumerate(nums):
            val = target - num
            if val not in dict:
                dict[num] = index
            else:
                return [dict[val], index]


