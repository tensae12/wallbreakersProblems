class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for strs in ops:
            if strs == "C":
                s.pop()
            elif strs == "D":
                s.append(2 * s[-1])
            elif strs == "+":
                s.append(int(s[-1] + s[-2]))
            else:
                s.append(int(strs))
        return sum(s)


        