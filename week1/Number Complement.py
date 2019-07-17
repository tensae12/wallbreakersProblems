class Solution:
    def findComplement(self, num):
        x = "{0:b}".format(num)
        temp = ""
        print(x)
        for i in x:
            if i == "0":
                i = "1"
            else:
                i = "0"
            temp += i
        x = temp
        binar = int(x, 2)
        return binar
