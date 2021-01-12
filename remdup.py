class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## count how many item are removed
        k=0
        for i in range(1,len(nums)):
            if nums[i-k]==nums[i-1-k]:
                nums.pop(i-k)
                k+=1
        return(len(nums))