class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for num in nums1:
            index = nums2.index(num)
            for i in range(index, len(nums2)):
                found = False
                if num < nums2[i]:
                    stack.append(nums2[i])
                    found = True
                    break
            if found == False:
                stack.append(-1)
        return stack