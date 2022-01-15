#find max area in binary matrix, and you can swap entire col i with j 
#'1' means area =1
#algorithm is to form a matrix to record the height for each col
#and form a count matrix to record so if there are more than 1 count of a height, you can find an area of height*2

def max_rectangle(mat):

  ##1.for the height of each col, repalce mat in place
  #e.x 1st col, the height is 1,2,3,0 from bottom to top
  m,n =len(mat),len(mat[0])

  #this step calculates the max area in column-wise
  maxArea= 0
  for j in range(n):
    for i in range(m-2,-1,-1):
      if mat[i][j]==1: #if value=1
        mat[i][j] = mat[i+1][j]+1
        maxArea =max(maxArea,mat[i][j])
 
  """
  mat becomes
  [0, 4, 0, 1, 4],
  [3, 3, 0, 0, 3],
  [2, 2, 0, 2, 2],
  [1, 1, 1, 1, 1]
  """
  #2. calculate the hight for all columns, if two columns have same height,
  #they can form a rectangle
  count =[[0 for i in range(n)] for _ in range(m)]

  for i in range(m):
    for j in range(n):
      if mat[i][j]>0:
        count[i][mat[i][j]]+=1
        maxArea =max(maxArea, count[i][mat[i][j]] *mat[i][j])
  return maxArea
  
 
if __name__ == '__main__':
 
    mat = [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
 
    area= max_rectangle(mat)
 #max area is 9
