''''
https://leetcode.com/problems/valid-anagram/
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list=[]
        for i in s:
            list.append(i)
        for j in t:
            if j in list:
                list.remove(j)
            else:
                return False
        if len(list)!=0:
            return False
        else:
            return True    
        
#sol:

sorted_s = sorted(s)
sorted_t = sorted(t)
# becose they have to use all the chars thats why it will be same if not then its not anagram
print(sorted_s == sorted_t)
    

