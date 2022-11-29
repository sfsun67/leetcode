'''思路：
    观察：
    抽象：
    1. groupSizes = [3,3,3,3,3,1,3] 是给定信息。由此建立  自变量（成员） x 与 其因变量（组数）y 的映射关系。映上函数。
    2. 问题：不同的 x 是否为同一集合？ 求出所有的集合
    探索：
    1. 直觉上，做两部运算。
        第一步，讲相同size 的组放在一起，形成 “初级组juniorgroups” 。 此时，没有相同 size 的组将被划分出来，进入高级组 seniorgroups
            找出来  ；  放在一起 ；  删除原 成员 x  
            判断该初级组是否可以放入高级组 。 可以放入则放入，不可以放入则进入第二步。
        第二步，处理“初级组”。初级组一定是其 y 的倍数 z。这个倍数 z 就是此初级组的组数。分组后加入高级组
    猜测：
    高级组 seniorgroups为我们想要的结果
    论证：
'''
'''
变量


juniorgroups0 = 建立的初级组，如果初级组是不重复情况，则直接放入高级组，如果是重复情况，则分组放入高级组
juniorgroups1 = 其实是复制了 juniorgroups0，用作上面 set 集合的建立。 相同size 的 x 放入小组后，进行下一步判断。为放入高级组（2元）做准备。
seniorgroups 高级组

juniorgroups1  删除成员 x 之前，对删除 x 做一个备份，用于建立 setdel
setdel  是所有被删除元素的集合
'''

from ast import Del
#from distutils.command import clean

class Solution:
    def groupThePeople(self, groupSizes):
        juniorgroups1 = [] #初始化低级组  ？？？
        seniorgroups = []
        g = len(groupSizes)
        setdel0 = set()    
        setdel = set()
        for i in range (g) :
            n_senior = len(seniorgroups)
            #集合的自迭代不会写，就写了三行作为替代
            setdel0 = setdel
            setdel = {groupSizes[s] for s in juniorgroups1 }  #把删除的 x 放入 setdel 中，用作下一步，是否重复的判断
            setdel = setdel0.union(setdel)    

            juniorgroups0 = [ j for j in range(g) if (groupSizes[j] == groupSizes[i] and ((groupSizes[i] in setdel) == False)) ]  #找到所有的和 i 位置相同 size 的成员 x  ,ji 记录其位置j，方便下一步移动成员
            jun = len(juniorgroups0)
            if jun == groupSizes[i]:                               #???????会不会有组数溢出的情况;??这个 i 对不对？   可以直接放入高级组
                juniorgroups1 = [ juniorgroups0[k] for k in range(jun)]        #其实是复制了 juniorgroups0，用作上面 set 集合的建立。 相同size 的 x 放入小组后，进行下一步判断。为放入高级组（2元）做准备。
                seniorgroups.append(juniorgroups0)        #放入高级组
            elif jun != 0 :                   # 进入下一步分组
                juniorgroups1 = [ juniorgroups0[k] for k in range(jun)]        #其实是复制了 juniorgroups0，用作上面 set 集合的建立。 相同size 的 x 放入小组后，进行下一步判断。为放入高级组（2元）做准备。
                n = int((jun) / groupSizes[i] )  #  能分成几组
                for u in range(n):
                    juniorgroups2 = [ juniorgroups0[o] for o in range(groupSizes[i])  ]
                    seniorgroups.append(juniorgroups2)        #放入高级组
                    for p in range(groupSizes[i]):
                        del juniorgroups0[0]  #删除已经放入高级组的 x

        return(seniorgroups)

                


#groupSizes = [3,3,3,3,3,1,3]
groupSizes = [2,1,3,3,3,2]
s = Solution()
print(s.groupThePeople(groupSizes))




