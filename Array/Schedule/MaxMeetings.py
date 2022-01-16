#problem is to find the max number meetings needs for given time array
#if the next meetings start time less than end time, count increases by 1 because a new meeting scheduled
#else if end equals start, one meeting ended, count decreases by 1

time= [[0,30],[5,10],[10,15]]
def meetings(time):

  start = sorted(list(i[0] for i in time))
  end =sorted(list(i[1] for i in time))
  count =0
  maxcount =0
  i =0
  j=0
  while i<len(start):
    if start[i]<end[j]: #new meeting starts, not ended yet
      count+=1
      i+=1 
    else:
      #if a meeting starts at ending time, means the current meeting is about ending
      #at the same time, another meetings start
      count-=1
      j+=1
    maxcount=max(maxcount,count)
  return maxcount 

meetings(time)
