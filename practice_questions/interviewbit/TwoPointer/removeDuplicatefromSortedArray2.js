
module.exports = { 
	removeDuplicates2 : function(A){
        if (A.length==0 || A.length==1) {
            return A.length;
        }
        let new_index = -1;
        let count = 1
        let i= 1;
        let prev_ele = A[0];

        while (i<A.length) {
            if (A[i]===prev_ele && count>=2) {
                    count++;
                    if (new_index===-1) {
                        new_index = i;
                    }
            }
            else {
                if (A[i]!=prev_ele){
                    count = 1; 
                }else {
                    count++;
                }
                if (new_index!=-1){
                    A[new_index] = A[i];
                    new_index++;
                }
            }
            

            prev_ele = A[i];
            i++;
        }
        if (new_index!=-1){
            A.splice(new_index);
        }
        return A.length;    
           
	}
};

// const A=[1,1,1,2, 2,3];
// let A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ];
let A = [ 0, 0, 1, 2 ];
let x = removeDuplicates2(A);
console.log(x);
