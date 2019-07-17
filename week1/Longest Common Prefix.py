class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = "" #prefix to return
        if len(strs) == 0:
            return output
        for i in range(len(min(strs))): #looping through the smallest string
            char = strs[0][i] #each character in the smallest string
            if all(string[i] == char for string in strs): #if they are equal storing the characters
                output += char
            else:
                break
        return output