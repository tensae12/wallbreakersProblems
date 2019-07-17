class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        lst = sorted(nums)
        return sum(lst[::2])


        