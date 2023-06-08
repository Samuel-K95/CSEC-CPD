class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key= lambda item:item[0])
        j=0
        for i in range(len(intervals)):
            if j+1<len(intervals):
                if intervals[j][0]<=intervals[j+1][0] and intervals[j][1]>=intervals[j+1][1]:
                    intervals.remove(intervals[j+1])
                    j=j
                elif intervals[j][1]>=intervals[j+1][0]:
                    intervals[j][0],intervals[j][1]=intervals[j][0], intervals[j+1][1]
                    intervals.remove(intervals[j+1])
                    j=j
                else:
                    j+=1

        return(intervals)