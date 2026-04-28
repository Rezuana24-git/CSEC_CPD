class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]%2 != 0 and nums[j]%2 == 0:
                    nums[i] , nums[j] =nums[j],nums[i]
        return nums   
    """if len(nums)==1:
            return nums
        r1 = []
        r2 = []
        for x in nums:
            if x%2==0:
                r1.append(x)
            else:
                r2.append(x)
        return r1+r2 
      """
