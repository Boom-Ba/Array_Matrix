##problem : find index to replace 0 with 1 to get the max length of subsequence 
#of continuous ones 

##A= [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]

"""
algorithm: if value==1: count+=1
           else calculate the count if replace it with 1
e.x at index=0, if replace it with 1, we get count=1 
keep tracking, current_count, max_count
the position where previous zero locates, so we can get the count after replacement
"""
def replace_zero(A):
  if 0 not in A:
    return len(A),-1
  max_len =0
  max_idx=-1
  count=0
  prev_zero=-1 
  dp=[]
  for idx, value in enumerate(A):
    
    if value==1:
      count+=1
    else:
      count =idx-prev_zero
      prev_zero=idx
    if count>max_len:
      max_len=count
      max_idx=prev_zero
  return max_len,max_idx
A= [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
replace_zero(A)
      
     
