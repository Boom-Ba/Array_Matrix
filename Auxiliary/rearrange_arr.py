#reset array such that A[A[i]] equals to i
#algorithm: use auxiliary array to make the chance and copy back to original Array
class Solution:
	
	def rearrange(self, A: List[int]) -> None:
		# Write your code here...
		aux =[0]*len(A)
		for i in range(len(A)):
			aux[A[i]] =i
		for i in range(len(aux)):
			A[i]=aux[i]
		return 
