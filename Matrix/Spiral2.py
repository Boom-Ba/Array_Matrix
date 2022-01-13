##Spiral matrix
#fill number into matrix with Spiral order form 1 to N
def generateMatrix(self, n: int) -> List[List[int]]:
        
  num=1 #fill the matrix from num 1: N
  #define the boundaries for 'while-loop'
  top , bottom =0, n-1
  left, right =0, n-1

  matrix =[[0 for _ in range(n)] for _ in range(n)]
  ##while-loop stops if there is no space left in matrix

  while top<=bottom and left <=right:
      #fill top row
      for j in range(left,right+1):
          matrix[top][j] =num
          num+=1
      top+=1 #update top boundary
      
      for i in range(top,bottom+1):
          matrix[i][right]=num
          num+=1
      right-=1
      
      for j in range(right,left-1,-1):
          matrix[bottom][j]=num
          num+=1
          
      bottom-=1
      for i in range(bottom,top-1,-1):
          
          matrix[i][left]=num
          num+=1
      left+=1
  return matrix
