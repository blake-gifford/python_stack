/* 
    Array: Binary Search (non recursive)
    Given a sorted array and a value, return whether the array contains that value.
    Do not sequentially iterate the array. Instead, ‘divide and conquer’,
    taking advantage of the fact that the array is sorted .
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;


// function binarySearch(sortedNums, searchNum) {
//     for( var i = 0; i < searchNums.length; i++){
//         len = sortedNums.length
//         var middle = Math.floor(len) / 2;

//     }
// }

function binarySearch(sortedNums, searchNum) {
    var start = 0;
    var end = sortedNums.length -1;
    while (start <= end){
        var middle = Math.floor((start + end) / 2);
        if( sortedNums[middle] < searchNum){
            return middle
        }
        else if(sortedNums[middle] < searchNum){
            start = middle + 1;
        }
        else{
            end = middle - 1;
        }
    }
    
}
binarySearch(nums1, searchNum1)