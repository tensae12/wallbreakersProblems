class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        rev = [words[::-1] for words in x]
        new = " ".join(rev)
        return new




            