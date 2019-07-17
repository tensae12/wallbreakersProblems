class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for num in range (left, right+1):
            for digits in str(num):
                if int(digits) == 0 or num % int(digits) != 0:
                    break
            else:
                output.append(num)
        return output









           