# 自分で書いてみる

# まず問題文の前提をしっかりと理解できていない、この場合は数字が入った配列で同じ数字があるかどうかの判定だね、まぁ文字でもできるけど、ともかく配列ね

class Solution:
  
  def containesDupulicate(self, nums: List[int]) -> bool:
    # corner case: nums is empty or size 1, return false
    if len(nums) <= 1:
      return False
    
    # step1: single linear scan left -> right, build as we go
    map = {}
    
    for num in nums:
      # step2: if map containes key that the elements is going in roop, then dup found so return true
      if num in map:
        return True;
      
      map[num] = True
      
    return False
  
# visualize when going the roop
'''
testcase 1
before:
  array:[1,3,5,4,3,6]
  map:{}
after: 
  array:[1,3,5,4,3,6]
  map:{1:True}
  
testcase 2
before:
  array:[1,3,5,4,3,6]
  map:{1:True}
after: 
  array:[1,3,5,4,3,6]
  map:{1:True, 3:True}
  
testcase 3
before:
  array:[1,3,5,4,3,6]
  map:{1:True, 3:True, 5:True}
after: 
  array:[1,3,5,4,3,6]
  map:{1:True, 3:True, 5:True, 4:True}
  
testcase 4
before:
  array:[1,3,5,4,3,6]
  map:{1:True, 3:True, 5:True, 4:True}
after: 
  array:[1,3,5,4,3,6]
  map:{1:True, 3:True, 5:True, 4:True, 3:False} ← in this case we found dupand the func return false
'''