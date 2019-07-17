class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range(len(A[0])):
            inside_A = []
            for j in range(len(A)):
                inside_A.append(A[j][i])
            output.append(inside_A)
        return output
