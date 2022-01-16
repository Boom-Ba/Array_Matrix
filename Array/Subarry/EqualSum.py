#find the Max length of subarray in x and y, such as they have the equal sum subarray
#algorithm is to use auxiliary array to keep track the sum_diff : x[:i] -y[:i]
#use a hashmap to record sum_difference 
# ** if difference appears before at i, means from i to j, adding these elements, the sub difference remain same
#so subarray x[i:j] and y[i:j] have equalSum. 
x= [0, 1, 0, 1, 0, 0]
y= [1, 1, 0, 0, 1, 1]

def longest_subarr(x,y):
  if not x or not y:
    return 0
  if len(x) ==len(y) and sum(x)==sum(y):
    return len(x)
  elif len(x)==len(y) ==1 and x[0]==y[0]:
    return 1
  maxlen =0
  sum0 =0
  sum1 =0
  d= {}
  d[0]=-1 #handle the subarray starts from index 0
  for i in range(len(x)):
    sum0+=x[i]
    sum1+=y[i]
    diff= sum0 -sum1
    # if diff==0 and diff not in d:
    #   maxlen =max(maxlen)
    if diff not in d:
      d[diff] = i #which means at index x, we got the difference between x_sum
                  #y_sum 
    else: 
      maxlen = max(maxlen,i-d[diff]) #if the diff has been seen before, means at current index
                         #the difference between x_sum and y_sum is same as before
  return maxlen 

maxlen =longest_subarr(x,y)
print(maxlen)
