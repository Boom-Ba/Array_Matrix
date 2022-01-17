import sys
class Solution:
  """
  Have auxiliary array to store 
  left _ i: Sum of subarray before ith elements, so last element won't have right sum 
  right_ i: Sum of subarray after ith elements 
  Max abs difference = min Left sum (i) - Max right Sum(i+1) or 
            max Left sum(i) - min right sum(i+1) 
  so algorithm is to use 4 auxiliary array to store MaxLeft, MaxRight, MinLeft, MinRight
  then do the math
  """
  """
    [-3, -2, 6, -3, 5, -9, 3, 4, -1, -8, 2]
    -3  -5,-2 
  """
  def maxSubArray(self, nums, aux_arr,reverse):
    if not nums:
      return 
    if reverse==False:
      max_ending_here= max_so_far =nums[0]
      aux_arr[0] =max_so_far 
      for i in range(1,len(nums)):
        max_ending_here=max(nums[i]+max_ending_here,nums[i])
        max_so_far =max(max_so_far,max_ending_here)
        aux_arr[i] =max_so_far 
    else:
      max_ending_here =max_so_far =nums[-1]
      aux_arr[-1] =max_so_far 
      for i in range(len(nums)-2,-1,-1):
        max_ending_here=max(nums[i]+max_ending_here,nums[i])
        max_so_far =max(max_so_far,max_ending_here)
        aux_arr[i] =max_so_far 
    return aux_arr
    
  def findMaxAbsDiff(self, nums) :
    n =len(nums)
    if not nums:
      return 0 
    if len(nums) ==1:
      return nums[0]
    reverse =False 
    MaxLeft =[-sys.maxsize]* n
    aux_arr = MaxLeft.copy()
    MaxLeft = self.maxSubArray(nums,aux_arr,reverse)
    MaxRight =[-sys.maxsize]* n
    aux_arr = MaxRight.copy()
    MaxRight = self.maxSubArray(nums,aux_arr,not reverse)
    
    MinLeft =[-sys.maxsize]* n
    nums =list(i*(-1) for i in nums)
    aux_arr = MinLeft.copy()
    MinLeft = self.maxSubArray(nums,aux_arr, reverse)
    MinLeft =list(i*(-1) for i in MinLeft)
    nums =list(i*(-1) for i in nums)

    
    MinRight =[-sys.maxsize]* n
    nums =list(i*(-1) for i in nums)
    aux_arr = MinRight.copy()
    MinRight = self.maxSubArray(nums,aux_arr,not reverse)
    nums =list(i*(-1) for i in nums)
    MinRight =list(i*(-1) for i in MinRight)

    # print(MaxLeft)
    # print(MinRight)
    # print(MaxRight) 
    # print(MinLeft)
    maxdiff = -sys.maxsize
    for i in range(n-1):
      maxdiff =max(maxdiff, abs(MaxLeft[i]-MinRight[i+1]), abs(MinLeft[i]-MaxRight[i+1]))
    return maxdiff
