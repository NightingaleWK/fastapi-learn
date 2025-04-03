# -*- coding: utf-8 -*-

# 创建一个列表
# 列表是 Python 中最常用的数据结构之一，可以存储任意类型的元素，并且元素可以修改。
my_list = [1, "你好", 3.14, True]
print(f"初始列表: {my_list}")

# 访问列表元素
# 列表索引从 0 开始
first_element = my_list[0]
second_element = my_list[1]
print(f"第一个元素: {first_element}")
print(f"第二个元素: {second_element}")

# 修改列表元素
my_list[1] = "世界"
print(f"修改后的列表: {my_list}")

# 向列表末尾添加元素
my_list.append(False)
print(f"添加元素后的列表: {my_list}")

# 在指定位置插入元素
# 在索引 2 的位置插入元素 "Python"
my_list.insert(2, "Python")
print(f"插入元素后的列表: {my_list}")

# 删除列表元素
# 删除指定索引的元素
del my_list[3]
print(f"删除索引 3 的元素后的列表: {my_list}")

# 删除第一个匹配的指定值的元素
my_list.remove('世界')
print(f"删除元素 世界 后的列表: {my_list}")

# 获取列表长度
list_length = len(my_list)
print(f"列表的长度: {list_length}")

# 列表切片
# 获取从索引 1 到索引 2 (不包括 3) 的元素
sub_list = my_list[1:3]
print(f"列表切片 [1:3]: {sub_list}")

# 检查元素是否存在于列表中
is_present = "世界" in my_list
print(f"'世界' 是否在列表中? {is_present}")

# 列表迭代
print("遍历列表中的元素:")
for item in my_list:
  print(item)

# 创建一个空列表
empty_list = []
print(f"这是一个空列表: {empty_list}")

# 列表嵌套
nested_list = [1, 2, [3, 4, 5], 6]
print(f"嵌套列表: {nested_list}")
print(f"访问嵌套列表中的元素: {nested_list[2][1]}") # 输出 4