'''
1. 总得思路是 for 循环，对 判断数字。因为数字只有10个，字母26个。❎
    ✔️ ： 判断类型是否为数字
2. 数字放在奇数位，非数字（字母）放在偶数位
3. 最终，计算奇偶位置的基数是否相差一，否，则返回 an empty string 


from difflib import restore
from ntpath import join
from turtle import TurtleGraphicsError


def reformat(str):
    n = len(str)
    transliststr = list(str)
    relist = [0]*2*n   #应该是 [0]*n 的  问题没有搞清楚
    print(relist)
    j=1
    k=0
    for i in range(n):
        if type(transliststr[i]) is int:   #list 中字符的数字是否自动转换为数字？
            relist[j] = transliststr[i]   #  是数字就放入奇数位
            j = j+2  #记录数字基数
        else:
            relist[k] = transliststr[i]     #  不是数字就放入偶数位
            k = k+2  #记录字母基数
    print(relist) 
    restr = ''.join(relist)
    if abs(j-k) == 1 :
        return(restr)
    else:
        return('')

str = 'a0b1c2'
print(reformat(str))
'''





def reformat(s:str):
        sumDigit = sum(c.isdigit() for c in s)  #这种用法还是第一次见  迭代的思想解决计数问题
        sumAlpha = len(s) - sumDigit
        if abs(sumDigit - sumAlpha) > 1:
            return ""
        flag = sumDigit > sumAlpha
        t = list(s)
        j = 1
        for i in range(0, len(t), 2):
            if t[i].isdigit() != flag:
                while t[j].isdigit() != flag:
                    j += 2
                t[i], t[j] = t[j], t[i]
        return ''.join(t)    

str = 'a0b1c2'
print(reformat(str))

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/reformat-the-string/solution/zhong-xin-ge-shi-hua-zi-fu-chuan-by-leet-lgqx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
