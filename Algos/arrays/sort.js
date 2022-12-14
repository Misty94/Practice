// Kenia's Whiteboarding Question:


// sort in ascending 


nums = [2,3,4,6,7,8,9,5]
temp = 0
for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
        if(nums[j] > nums[j+1]) {
            temp = nums[j];
            nums[j] = nums[j+1];
            nums[j+1] = temp;
        }
    }
}
console.log(nums);

// output
// [2, 3, 4, 5, 6, 7, 8, 9]