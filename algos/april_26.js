function multArr(nums) {
    // BASE CASE - where should i stop
    if (nums.length < 1) return 1;
  
    // FORWARD PROGRESS
    newArr = nums.slice(1, nums.length)
  
    // RECURSIVE CALL
    return nums[0] * multArr(newArr)
}
  
  
  /* 
    Recursively sum an arr of ints
  */
  
    const nums1 = [1, 2, 3];
    const expected1 = 6;
  
function sumArr(nums) {
    if (nums.length < 1) return 1;

    newArr = nums.slice(1, nums.length)

    return nums[0] * sumArr(newArr)
}
sumArr()
  /*****************************************************************************/
  
  /* 
    Recursive Sigma
    Input: integer
    Output: sum of integers from 1 to Input integer
  */
  
  const num1 = 5;
  const expected1 = 15;
  // Explanation: (1+2+3+4+5)
  
  const num2 = 2.5;
  const expected2 = 3;
  // Explanation: (1+2)
  
  const num3 = -1;
  const expected3 = 0;
  
  function recursiveSigma(num) {}