// // // Array.prototype.myMethod = function(){
// // //     for (i = 0; i<this.length; i++){
// // //         this[i]= this[i].toUpperCase();
// // //     }
// // // }

// // // var 

// // var object = {
// //     x:1,
// // //     y:2,
// // //     z:this.x  + this.y,
// // //     sum: function() {
// // //         return this.x + this.y;
// // //     }
// // // }

// // // var sum = object.sum;
// // // console.log(sum());
// // // console.log(object.sum());

let num = 1;
function myFunction() {
    for (var i =0; i<4;i++){
        num +=2;
        return yourFunction(num);
    }
}

function yourFunction(x){
    x-=1;
    if (x==2) return x++;

}
console.log(myFunction());

// var j =4;
// var i =1;

// for (i=1; i<3;i++){
//     while(j>0){
//         if (i*j ==8){
//             continue;
//         }
//         if (i*j==27){
//             break;
//         }     
//         console.log(i*j);
//         j--;
//     }
// }

// console.log(i+j);

// if (isNaN(0/0)){
//     alert("A")
// }
// else{
//     alert("B");
// }


