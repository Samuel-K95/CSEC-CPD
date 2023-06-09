class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arranged=[]
        left=0
        right=len(nums)-1

        while left<right:
            arranged.append(nums[left]+ nums[right])
            left+=1
            right-=1
        return(max(arranged))