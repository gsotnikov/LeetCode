class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Naive time O(N^2), Memory O(1)
#         max_num = sum(nums)
#         for i in range(len(nums)):
#             curr = nums[i]
#             if curr > max_num:
#                 max_num = curr
            
#             for j in range(i+1, len(nums)):
#                 curr += nums[j]
                
#                 if curr > max_num:
#                     max_num = curr
                    
#         return max_num

        # Dynamic Programming, Kadane's Algorithm
        
        # Time complexity: O(N), Space complexity: O(1)
        curr_max = absolute_max = nums[0]
        for num in nums[1:]:
            # curr_max = max(num, curr_max + num)
            if num > curr_max + num:
                curr_max = num
            else:     
                curr_max = curr_max + num
                
            absolute_max = max(curr_max, absolute_max)
        return absolute_max