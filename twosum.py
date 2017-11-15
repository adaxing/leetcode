class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic.update({i: nums[i]})   
            for k,v in dic.items():
                if v+nums[i] == target:
                    if k!=i:
                        result.append(k)
                        result.append(i)
                        return result

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))