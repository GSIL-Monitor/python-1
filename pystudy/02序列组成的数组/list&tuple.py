# 列表（list） 和 元组（tuple） 的所有基础
# 列表是可改变的，元组是不可改变的
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d','e']
# 创建了L1和L2这两个列表
# 查看
print(L1[0],L2[0])
# 打印第一个元素 1
print(L1[1:3],L2[1:3])
# 打印第2和第3个元素，不包括第4个 [2,3]
print(L1[:2],L2[:2])
# 打印从首位开始的2个
print(L1[2:],L2[2:])
# 打印除末位开始的2个
print(L1,L2)
# 打印所有
# 排序和反向
L1.sort()
# 排序： [1, 2, 3, 4, 5]
L1.reverse()
# 反向列表元素： [5, 4, 3, 2, 1]
# 增加
L1.append(1)
# 增加1的L1： [5, 4, 3, 2, 1, 1]
L1.extend(L2)
# 扩展后的L1： [5, 4, 3, 2, 1, 1, 'a', 'b', 'c', 'd', 'e']
# 更新
L1[1]=20
# 更新后 [5, 20, 3, 2, 1, 1, 'a', 'b', 'c', 'd', 'e']
# 删除
L1.pop()
# 删除最后一位: [5, 20, 3, 2, 1, 1, 'a', 'b', 'c', 'd']
L1.remove(3)
# 移除3: [5, 20, 2, 1, 1, 'a', 'b', 'c', 'd']
del L1[0]
# 删除第一位 [20, 2, 1, 1, 'a', 'b', 'c', 'd']
# 其他
print('第一次出现2的地方：',L1.index(2))
print('1出现的次数：',L1.count(1))
print('----------------------')
# 元组   不可修改
T1 = (1,2,3,4,5)
T2 = ('a','b','c','d','e')
print(T1[0],T2[0])
# 打印第一个元素 1
print(T1[1:3],T2[1:3])
# 打印第2和第3个元素，不包括第4个 [2,3]
print(T1[:2],T2[:2])
# 打印从首位开始的2个
print(T1[2:],T2[2:])
# 打印除末位开始的2个
print(T1,T2)

L3 = [1,[2,3,[4,5]]]
print(L3)