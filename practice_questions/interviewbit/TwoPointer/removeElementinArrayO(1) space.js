module.exports = { 
	//param A : array of integers
	//param B : integer
	//return an integer
	removeElement : function(A, B){
        let count = 0
        for (let i=0; i<A.length; i++){
            if (A[i] != B){
                A[count] = A[i];
                count++;
            }
        }
        return count
	}
};
