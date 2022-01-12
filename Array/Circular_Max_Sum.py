"""
find max sum of circular array
Input:  {2, 1, -5, 4, -3, 1, -3, 4, -1}
 
Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.

"""

A= [2, 1, -5, 4, -3, 1, -3, 4, -1]

def maxSum(A):
  max_ending_here= 0
  global_max=max(A)

  for i in range(len(A)):
    max_ending_here +=A[i]
    max_ending_here =max(max_ending_here, 0)
    if max_ending_here>global_max:
      global_max=max_ending_here
  return global_max
def circular_max_sum(A):
  max_Res= max(A)
  for i in range(len(A)):
    T =A[i:]+A[:i] #make circular _array
    #call max_Sum
    res = maxSum(T)
    if res>max_Res:
      max_Res=res
  return max_Res
# circular_max_sum(A)  output:6
