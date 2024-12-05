// You are given a string s representing an attendance record for a student 
// where each character signifies whether the student was absent, late, or present on that day. 
// The record only contains the following three characters:

// 'A': Absent.
// 'L': Late.
// 'P': Present.
// The student is eligible for an attendance award if they meet both of the following criteria:

// The student was absent ('A') for strictly fewer than 2 days total.
// The student was never late ('L') for 3 or more consecutive days.
// Return true if the student is eligible for an attendance award, or false otherwise.

/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function (s) {
    let late = 1;

    let arr_s = s.split('');
    let absent = arr_s[0] === "A" ? 1 : 0;
    res = 0;
    for (let i = 1; i < arr_s.length; i++) {
        let prev_element = arr_s[i - 1];
        let element = arr_s[i];
        if (element === "L" & prev_element === "L") {
            late += 1;
            res = late > 2 ? 1 : 0;
        } else {
            late = 1;
        }

        if (element === "A") {
            absent += 1;
            res = absent > 1 ? 1 : 0;
        }

        if (res > 0) {
            return false;
        }
    };
    return true;
};
