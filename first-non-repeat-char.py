from re import M


class Solution:
  
  def firstNonRepeatChar(self, chars: List[str]) -> int:
    # corner case: chars is empty or size 1, return false:
    if len(chars) <= 1:
      return False
    
    # step1: in single linear scan left -> right build {eachChar: count} as we go 
    map = {}
    
    for char in chars:
      if char in map:
        map[char] += 1
      else:
        map[char] = 1
      
    # step3: chack the map key where value is 1
    for i in len(chars):
      if map[chars[i]]:
        return map[i]
      
    return -1