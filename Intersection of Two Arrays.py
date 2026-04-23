class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for num in nums1:
            if num in nums2:
                arr.append(num)
        s=set(arr)
        return list(s)
