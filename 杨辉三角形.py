
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    yangh = list() #生成杨辉三角形的基本数据结构
    for i in range(numRows):#生成numrows行 0,1,2,3,4
        row0 = list()
        for j in range(i+1):#生成每一行的数字 0
            
            if j == 0 or j == i:  #第一列或最后一列为1
                #yangh[i][j] = 1           #使用append方法，将元素一个个的加入，最大化利用python特性。降低出现bug的概率（eg数组溢出）
                row0.append(1)
            else:
                #yangh[i][j] = yangh[i-1][j-1] + yangh[i-1][j]
                row0.append(yangh[i-1][j-1] + yangh[i-1][j])
        yangh.append(row0)
    return yangh

print(generate(numRows=5))

