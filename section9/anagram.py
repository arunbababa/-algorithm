from operator import truediv


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        # initial corner case
        if not s and not t: # both are empty so it means they can be anagram
          return True
        if not s or not t: # either one is empty so it means they cant be anagram
          return False
        if len(s) != len(t): # the length is different in s and t, it means they cant be anagram
          return False
        
        # step1: linear scan s from left => right, build map like {each_char:count}
        map = {}
        
        for s_char in s:
          if s_char in map:
            map[s_char] += 1 # if already exsist, add 1 in the exsist count value
            continue
          map[s_char] = 1 # if apper for the first time, init the count value with 1
          
        # step2: linear scan t from left => right, subtraction -1 from the value count of map, if t_char in map keys
        # corner case
        for t_char in t:
          if t_char not in map: # if t_char doesnt exist in map keys, it means each str doesnt have same char, so return false quickly
            return False
          map[t_char] -= 1
          
        # step3: check the maps each count value, if all is 0, it means both str has same str, same times, so it can be anagram.
        for i in map:
          if map[i] != 0:
            return False
        return True
          