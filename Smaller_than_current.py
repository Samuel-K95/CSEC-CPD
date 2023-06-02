class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            max=nums[i]
            count=0
            for j in range(len(nums)):
                if i==j:
                    continue
                elif max>nums[j]:
                    count+=1
            answer.append(count)

        return(answer)