class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                x = "FizzBuzz"
            elif x % 3 == 0:
                x = "Fizz"
            elif x % 5 == 0:
                x = "Buzz"
            else:
                x = str(x)
            result.append(x)
        return result

            