# key: image two pointer separating the nums, image the border
from ast import List
from pdb import run


class Solution:
  # move all zero toward the end, while maintaining non-zero item order
  # pre: nums[0,1,0,3,12]
  # post: nums[1,3,12,0,0]
  def move_zeros(self, nums:List[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
        
    def swap(nums: List[int], i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]
    
    # step1: linear scan left -> right while runnerIndex < nums.length
    nonZeroLastIndex = 0
    runner = 0 # it goes through nums and check if there is non-zero num, if it swap with nums[nonZeroLastIndex]
    
    # step2: split array into two sections. non-zero and zero sections using two indices
    while runner < len(nums):
      
      # step3: if nums[runnerIndex] != 0, then swap(nums[nonZeroLast], nums[runnerIndex])
      if nums[runner] != 0:
        swap(nums, nonZeroLastIndex, runner)
        nonZeroLastIndex += 1
        
      runner += 1
    