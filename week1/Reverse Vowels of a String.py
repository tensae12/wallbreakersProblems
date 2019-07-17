class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        i = 0
        v = ""
        v2 = ""
        for char in s:
            if char.lower() in vowels:
                v += char
                char = "#"

        print(s)








