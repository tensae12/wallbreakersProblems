class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            l = len(output)
            for i in range(l):
                output.append(output[i] + [num])
        return output