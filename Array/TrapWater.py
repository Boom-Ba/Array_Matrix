"""
Trap water : Given an array represents the height of bars, output the max amount of water that can be trapped

Hint: for a place that water can be trapped, we can observe the minimal height of (max height before this bar, max height after this bar) 

is higher than the height of the bar.
So use two array, one array for recording the max_height before current bar, and another array for recording the max_height after current bar.
And take the minimal of them to see if water can be trapped in the current location. 
"""

def trapWater(bars):
  n=len(bars)

  left_max_heights =[-float('inf')]+[0]*(n-1)
  right_max_heights=[0]*(n-1)+[-float('inf')]

  #max height left to bars[i]
  for i in range(1,n):
    left_max_heights[i] = max(bars[i-1],left_max_heights[i-1])

  for i in range(n-2,-1,-1):
    right_max_heights[i] = max(bars[i+1],right_max_heights[i+1])

  res = 0
  for i in range(n):
    if min(left_max_heights[i],right_max_heights[i]) >bars[i]:
      res+=min(left_max_heights[i],right_max_heights[i]) - bars[i]

  return res

a= [10, 8, 6, 5, 4, 2]
res=trapWater(a) #output 0, cannot trap any water
