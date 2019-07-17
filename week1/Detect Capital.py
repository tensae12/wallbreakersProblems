class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if (word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower()) == True):
            return True
        else:
            return False

        