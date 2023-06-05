class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            import math

            def dist(list1):
                x=math.hypot(list1[0], list1[1])
                return x
            store={i:dist(points[i]) for i in range(len(points))}
            answer=dict(sorted(store.items(), key= lambda item:item[1]))
            ans=[]
            j=0
            for i in answer:
                if j>=k:
                    break
                ans.append(points[i])
                j+=1
            return(ans)