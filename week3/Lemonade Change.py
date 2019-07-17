class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = c10 = c20 = 0
        for bill in bills:
            if bill == 5:
                c5 += 1
            elif bill == 10:
                c5 -= 1
                c10 += 1
            elif bill == 20:
                if c10 > 0:
                    c10 -= 1
                    c5 -= 1
                else:
                    c5 -= 3
            if c5 < 0:
                return False
        return True
                    