# Given an integer array and an integer k, 
#shrink it by removing adjacent triplets that 
#satisfy the given constraints and return the left number of elements in the resultant array.
class Solution:
	def shrink(self, nums: List[int], k: int) -> int:
		
		##recursion on each ele in nums

		#two cases:

		#1.include the current element in triplet
		#2.not 

		def solve(start,end, nums):
			if start>end:
				return 0
			#1.exclude, because it doesn't satisfy condition, cannot form a triplet
			res = solve(start+1,end,nums)+1 
			
			#2.to form a valid triplet (start, i, j)
			for i in range(start+1,end):
				for j in range(i+1,end+1):#check condition 
					if nums[start]+k==nums[i] and nums[i]+k ==nums[j]:
						if not solve(start+1,i-1,nums) and not solve(i+1,j-1,nums):
						#found a tuplet
							n= solve(j+1,end,nums)
					
							res= min(n,res)
			return res
		return solve(0,len(nums)-1, nums)
