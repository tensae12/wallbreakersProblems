class Solution:
    def binaryGap(self, N: int) -> int:
        last = None
        x = 0
        binary = "{0:b}".format(N)
        for i in range(len(binary)):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(x, i - last)
                last = i
        return x