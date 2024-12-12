// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving 
// the order of characters. No two characters may map to the same character, but a character may map to itself.

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
    let arr_s = s.split("");
    let arr_t = t.split("");
    let map_s = {};
    let map_t = {};
    let res = "";

    for (let i = 0; i < arr_s.length; i++) {
        if (map_s[arr_s[i]] !== undefined & map_t[arr_t[i]] === undefined) {
            return false;
        } else {
            if (map_s[arr_s[i]] === undefined & map_t[arr_t[i]] !== undefined) {
                return false;
            }
        }
        if (map_s[arr_s[i]] === arr_t[i] & map_t[arr_t[i]] === arr_s[i]) {
            res += map_s[arr_s[i]];
        } else {
            if (map_s[arr_s[i]] === undefined) {
                map_s[arr_s[i]] = arr_t[i];
            }
            if (map_t[arr_t[i]] === undefined) {
                map_t[arr_t[i]] = arr_s[i];
            }
            res += map_s[arr_s[i]];
        }
    }
    return res === t;
};
