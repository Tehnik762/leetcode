# You are given an integer money denoting the amount of money (in dollars)
# that you have and another integer children denoting the number of children
# that you must distribute the money to.
#
# You have to distribute the money according to the following rules:
#
# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars
# if you distribute the money according to the aforementioned rules. If
# there is no way to distribute the money, return -1.

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        test = money/children
        if test >= 1:
            res = 0
            while True:
                if money >= 8 and children > 0 and children < money:
                    money -= 8
                    res += 1
                    children -= 1
                else:
                    if money == 0 and children == 0:
                        return res
                    if money == 4 and children == 1:
                        return res - 1
                    if money >= children and children != 0:
                        return res
                    else:
                        while children >= 0:
                            if res > 0:
                                res -= 1
                                children -= 9
                                if money >= children or children == 0:
                                    return res
                            else:
                                return 0
                        return res
        else:
            return -1



