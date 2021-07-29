// https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

module.exports = { 
	//param A : array of integers
	//return an integer
	removeDuplicates : function(A){
        let index = 0;
        let i = 0;
        while (i<A.length) {
            A[index] = A[i];
            i++;
            while (i<A.length && A[i]=== A[i-1]) {
                i++;
            }
            index++;

        }
        return index;
     
	}
};

const A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3 ];

console.log(removeDuplicates(A));