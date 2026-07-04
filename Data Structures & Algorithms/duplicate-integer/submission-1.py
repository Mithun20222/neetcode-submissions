class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        rep = False
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                rep = True
        return rep