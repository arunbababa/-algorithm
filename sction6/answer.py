class Solution:
    # move all zeros toward the end, while maintaining non-zero item order
    # pre: nums[0,1,0,3,12]
    # post: nums[1,3,12,0,0]
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
 
        def swap(nums: List[int], i: int, j: int):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
 
        # step1: linear scan left -> right while runnerIndex < nums.length
        nonZeroLastIndex = 0
        runner = 0
        
        # testcases: nums[], nums[1], nums[1,3], nums[1,3,0], nums[0], nums[0,3], nums[1,0,3]
        while runner < len(nums):
            # step 2: split array into two sections, non-zero and zero sections using two indeces
        
            # step 3: if nums[runnerIndex] != 0, then swap(nums[nonZeroLast], nums[runnerIndex])
            if nums[runner] != 0:
                swap(nums, nonZeroLastIndex, runner)
                nonZeroLastIndex += 1
 
            runner += 1