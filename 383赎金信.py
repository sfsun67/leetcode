# 为啥我的代码几乎是耗时最长和用内存最多的

def canConstruct(ransomNote, magazine):
    listmagazine = list(magazine)
    n = len(ransomNote)
    for i in range(n):
        m = len(listmagazine)
        for j in range(m):
                if ransomNote[i] == listmagazine[j]:       #list 和  str 中的字符可以比较嘛？
                    print(f"字串符是{[i]}：{ransomNote[i]}  列表是{[j]}:{listmagazine[j]}")
                    del listmagazine[j]                            #如果匿名信中字母和杂志中相同，则删除这个字符。
                    break                                      #跳出循环避免重复删除
                if j == m-1:
                    return(False)
        if m == 0 and n != 0:     # 补充一种情况 ， 杂志中已经是空集了，而匿名信还没写完 
            return(False)
    return(True)





ransomNote = "abc"
magazine = "ab"
bool0 = canConstruct(ransomNote , magazine)
print(bool0)