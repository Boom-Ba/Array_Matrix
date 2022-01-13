#fill matrix with clockwise direction [right, down, left, up ... ] 
#may reach out of matrix boundary and may return back to the boundary later
#tips: update the length of currently visiting direction and check the boundary of matrix

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """
    clockwise direction d=[0,1,0,-1,0]
                            0 1 2  3 -- means 4 directions
        """
        n =rows*cols ##total number of rows in matrix
        mat =[[0,0] for _ in range(n)]
        
        mat[0]=[rStart,cStart]
        dir_=[0,1,0,-1,0]
        num=1
        d=0 #current direction is toward east
        l_ =0 
        i=1
        while i<n: #number of rows in matrix
            if d ==0 or d==2:
                l_+=1 #every time toward to east, the len +=1
           
            for k in range(l_):
                rStart+=dir_[d]
                cStart+=dir_[d+1]
                if 0<=rStart<rows and 0<=cStart<cols:
                    mat[i]=[rStart,cStart]
                    i+=1    
            d=(d+1)%4

            
        return mat 
        
