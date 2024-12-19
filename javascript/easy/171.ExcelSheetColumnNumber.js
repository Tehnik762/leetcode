// Given a string columnTitle that represents the column title as appears 
// in an Excel sheet, return its corresponding column number.

// For example:

// A -> 1
// B -> 2
// C -> 3
// ...
// Z -> 26
// AA -> 27
// AB -> 28 
// ...
// columnTitle is in the range ["A", "FXSHRXW"].
//
//

//  ZY = (Z*26**1 + Y*26**0) = 26*26 + 25 =701


/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function (columnTitle) {
    const alphabet = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    res = 0;
    columns_list = columnTitle.split("").reverse();
    for (let i = 0; i < columns_list.length; i++) {
        res += alphabet.indexOf(columns_list[i]) * Math.pow(26, i);
    }
    return res;
};
