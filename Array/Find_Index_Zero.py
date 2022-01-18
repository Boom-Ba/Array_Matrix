
# Given a binary array, 
# find the index of 0 to be replaced with 1 to get the maximum length sequence of continuous ones. 
# return the index of first replaced 0

def findIndexofZero(self, nums: List[int]) -> int:
           """
           [1, 1, 1, 1, 0]
            1. 2. 3. 4   
           """

           prevZero =-1
           maxCount =0
           maxIndex=-1
           count=0
           for i in range(len(nums)):
                      if nums[i] ==0:
                                 count =i-prevZero
                                 prevZero =i
                      else:
                                 count+=1
                      if count>maxCount:
                                 maxIndex=prevZero
                                 maxCount=count 
           return maxIndex
