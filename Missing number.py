class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if max(nums) == len(nums):
            i=0
            while i < len(nums):
                if i != nums[i]:
                    return i
                i+=1
        else:
            return max(nums) + 1
