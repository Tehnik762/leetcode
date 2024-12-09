// Given an integer array nums and an integer k, return true if there are
//  two distinct indices i and j in the array such that nums[i] == nums[j] .
//  and abs(i - j) <= k.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
    let temp = {}
    for (let i = 0; i < nums.length; i++) {
        if (temp[nums[i]] !== undefined) {
            let test = i - temp[nums[i]];
            if (test <= k) {
                return true
            } else {
                temp[nums[i]] = i;
            }
        } else {
            temp[nums[i]] = i;
        }
    }
    return false;
};
