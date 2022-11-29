"""给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。

「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-score-after-splitting-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
题解：


'''

class Solution:
    def maxScore(self, s: str) :
        r_score = 0
        l_score = 0
        score = []
        n = len(s)
        list_s = list(s)
        list_s = list(map(int, list_s))
        for i in range(n):
            if list_s[i] == 0  and i != n-1:                     #解决左空集问题
                r_score += 1                        #左分割有几个0 则计数 几个
            l_score = sum(list_s[(i+1):])           #右分割有几个1 则计数几个, 根据分割原理，list 计数为i+1，解决“1111“左分割空集问题
            score.append(r_score + l_score)
            del l_score                             #清零右分割，反之影响下一个计数
        maxscore = max(score)
        return( maxscore )
            



#s = "0100"
#s = "00111"
#s = "1111"
solu = Solution()
print(solu.maxScore(s))