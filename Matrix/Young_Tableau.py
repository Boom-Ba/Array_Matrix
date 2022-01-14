 ##create a matrix that
 
 ##1. each row is sorted as an increasing order
 ##2. each col is sorted as an increasing order 
 
#  Output: [
# 	[10, 11, 12, 15],
# 	[16, 18, 20, 22],
# 	[25, 27, 30, 34],
# 	[35, 40, 44, 45]
# ]
 class Solution:
	def constructYoungTableau(self, keys: List[int]) -> List[List[int]]:
		# Write your code here...
		m=n =ceil(sqrt(len(keys)))
		
		#insert from bottom-right toward top-left
		def insert(i,j,t):
			if i==0 and j==0:
				return
			
			if i==0:
				if t[i][j-1]>t[i][j]:
					t[i][j-1],t[i][j]=t[i][j],t[i][j-1]
					insert(i,j-1,t)
				return 
			
			if j ==0 :
				if t[i-1][j]>t[i][j]:
					t[i][j],t[i-1][j]=t[i-1][j],t[i][j]
					insert(i-1,j,t)
				return 
			
			if t[i-1][j]>t[i][j]:
				t[i][j],t[i-1][j]=t[i-1][j],t[i][j]
				insert(i-1,j,t)
			
			if t[i][j-1]>t[i][j]:
				t[i][j-1],t[i][j]=t[i][j],t[i][j-1]
				insert(i,j-1,t)
		
				
		t = [[float('inf') for _ in range(n)] for _ in range(m)]
		
		for k in keys:
			
			if t[m-1][n-1] !=float('inf'):
				return t
			else:
				t[m-1][n-1] =k
				insert(m-1,n-1, t)
		
		return t
