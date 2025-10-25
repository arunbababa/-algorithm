# key: image two pointer separating the nums, image the border


from typing import List


class Solution:
  # move all target val toward the end, while maintaining non-val item order
  # pre: nums[0,1,0,3,12]
  # post: nums[1,3,12,0,0]
  def move_zeros(self, nums: List[int], target_val: int):
    """
    Do not return anything, modify nums in-place instead.
    """
        
    def swap(nums: List[int], i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]
    
    # step1: linear scan left -> right while runnerIndex < nums.length
    nonValLastIndex = 0
    runner = 0 # it goes through nums and check if there is non-vsl num, if it swap with nums[nonValLastIndex]
    val = target_val
    # step2: split array into two sections. non-zero and zero sections using two indices
    while runner < len(nums):
      
      # step3: if nums[runnerIndex] != val, then swap(nums[nonValLastIndex], nums[runnerIndex])
      if nums[runner] != val:
        swap(nums, nonValLastIndex, runner)
        nonValLastIndex += 1
        
      runner += 1
      
    # return as blow because the result must be length of non-val sections length
    return nonValLastIndex
    