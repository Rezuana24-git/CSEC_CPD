class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        min=float("inf")
        for i in range(len(list1)):
            dic[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in dic:
                sum= j + dic[list2[j]]
                if sum < min:
                    min = sum
                    res=[]
                    res.append(list2[j])
                elif sum == min:
                    res.append(list2[j])

        return res     
