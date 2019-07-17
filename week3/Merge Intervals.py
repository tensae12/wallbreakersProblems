class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lst = []
        temp = []
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                temp.append(intervals[i][0])
                temp.append(intervals[i+1][1])
                lst.append(temp)
                #i += 2
                #temp = []
            else:
                lst.append(intervals[i])
        return lst

        