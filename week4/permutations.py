class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        lst = []
        for i in range(len(nums)):
            m = nums[i]
            rem_Lst = nums[:i] + nums[i+1:]
            for p in self.permute(rem_Lst):
                lst.append([m] + p)
        return lst