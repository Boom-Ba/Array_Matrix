#recursively build the young tableau matrix
#how? insert into the bottom-right corner of matrix, and recursively 
#insert into matrix, until it satisfy the property of young tableau
def young_tableau(n,keys):
  T = [[float('inf') for _ in range(n)] for _ in range(n)]
  def place(k,i,j):
    if i ==0 and j==0:
      return 
    if i==0:
      while j-1>=0 and T[i][j-1]>T[i][j]: #if element has been placed into the last index of first row, then check the column
        T[i][j-1] ,T[i][j] =T[i][j], T[i][j-1]
        j-=1
      return 
    if j==0:
      while i-1>=0 and T[i-1][j]>T[i][j]:
        T[i-1][j] ,T[i][j] =T[i][j], T[i-1][j]
        i-=1
      return 

    #place k upward
    if i-1>=0 and T[i-1][j]>T[i][j]:
      T[i-1][j] ,T[i][j] =T[i][j], T[i-1][j]
      place(k,i-1,j)
    if j-1>=0 and T[i][j-1]>T[i][j]:
      T[i][j-1] ,T[i][j] =T[i][j], T[i][j-1]
      place(k,i,j-1)
  

  for k in keys:
    if T[-1][-1]!=float('inf'):
      return T
    T[-1][-1] = k
    place(k,len(T)-1,len(T)-1)
  return T

if __name__ == '__main__':
  N = 3
  keys = [6, 4, 8, 7, 2, 3, 1, 5]
  T= young_tableau(N,keys)
  # sort(keys)
  sorted_keys= list(T[i][j]for i in range(len(T)) for j in range(len(T[0])))[:len(keys)]
  #output ->[1, 2, 3, 4, 5, 6, 7, 8]
