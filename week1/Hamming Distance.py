class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference = 0
        num = x ^ y
        binRep = "{0:b}".format(num)
        for i in binRep:
            if i == "1":
                difference += 1
        return difference


        