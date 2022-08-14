class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Dummy solution
        # return False if (len(set(nums)) == len(nums)) else True # hashmap = {}
        
        # Time complexity: O(n) Space complexity: O(n)
        hashmap = {}
        for number in nums:
            v = hashmap.get(n, None)
            if v:                
                return True
            else:
                hashmap[n] = 1
        return False