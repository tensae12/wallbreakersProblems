class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        not_duplicated = []
        for i in nums:
            if i not in not_duplicated:
                not_duplicated.append(i)
            else:
                not_duplicated.remove(i)
        return not_duplicated.pop()




        