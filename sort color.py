class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        cur=0
        high=len(nums)-1
        for i in range(len(nums)):
            if nums[cur] == 0:
                nums[cur],nums[low] = nums[low],nums[cur]
                cur+=1
                low+=1
            elif nums[cur] == 2:
                nums[cur],nums[high] = nums[high],nums[cur]
                high-=1
            else:
                cur+=1
