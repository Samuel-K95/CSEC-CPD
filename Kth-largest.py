class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=sorted(nums, key=lambda item:int(item))
        return(nums[len(nums)-k])