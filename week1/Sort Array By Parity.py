class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_list = [i for i in A if i % 2 == 0]
        odd_list = [i for i in A if i % 2 != 0]

        return even_list + odd_list

