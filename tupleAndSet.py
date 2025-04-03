# -*- coding: utf-8 -*-

# --- 元组 (Tuple) 示例 ---
# 元组是有序且不可变的序列。一旦创建，就不能修改其内容。

# 创建一个元组
my_tuple = (1, "你好", 3.14, True, 1) # 可以包含重复元素
print(f"初始元组: {my_tuple}")

# 访问元组元素 (与列表类似，使用索引)
first_element_tuple = my_tuple[0]
second_element_tuple = my_tuple[1]
print(f"元组的第一个元素: {first_element_tuple}")
print(f"元组的第二个元素: {second_element_tuple}")

# 尝试修改元组元素 (会引发 TypeError)
try:
    my_tuple[1] = "世界"
except TypeError as e:
    print(f"尝试修改元组时出错: {e}")

# 元组切片 (与列表类似)
sub_tuple = my_tuple[1:3]
print(f"元组切片 [1:3]: {sub_tuple}")

# 获取元组长度
tuple_length = len(my_tuple)
print(f"元组的长度: {tuple_length}")

# 检查元素是否存在于元组中
is_present_tuple = "你好" in my_tuple
print(f"'你好' 是否在元组中? {is_present_tuple}")

# 计算元素出现的次数
count_ones = my_tuple.count(1)
print(f"元素 1 在元组中出现的次数: {count_ones}")

# 查找元素第一次出现的索引
index_hello = my_tuple.index("你好")
print(f"元素 '你好' 的索引: {index_hello}")

# 元组打包和解包
packed_tuple = 4, 5, 6 # 打包
print(f"打包的元组: {packed_tuple}")
a, b, c = packed_tuple # 解包
print(f"解包后的变量: a={a}, b={b}, c={c}")

# 单元素元组 (注意需要逗号)
single_element_tuple = (10,)
print(f"单元素元组: {single_element_tuple}, 类型: {type(single_element_tuple)}")

print("\n" + "="*100 + "\n") # 分隔符

# --- 集合 (Set) 示例 ---
# 集合是无序且不包含重复元素的集合。

# 创建一个集合 (直接创建或从列表转换)
my_set = {1, 2, 3, "Python", 3} # 重复的 3 会被自动移除
print(f"初始集合: {my_set}")

list_for_set = [4, 5, 6, 4, "Java"]
set_from_list = set(list_for_set) # 从列表创建集合
print(f"从列表创建的集合: {set_from_list}")

# 添加元素到集合
my_set.add(7)
set_from_list.add("Python") # 可以添加已存在的元素，集合不变
print(f"添加元素后的集合 my_set: {my_set}")
print(f"添加元素后的集合 set_from_list: {set_from_list}")

# 从集合中移除元素
# remove() 如果元素不存在会引发 KeyError
my_set.remove(2)
print(f"移除元素 2 后的集合: {my_set}")

# discard() 如果元素不存在不会引发错误
set_from_list.discard(10) # 10 不存在，但不会报错
set_from_list.discard(4)
print(f"Discard 元素后的集合: {set_from_list}")

# 检查元素是否存在于集合中 (非常高效)
is_present_set = "Python111" in my_set
print(f"'Python111' 是否在集合 my_set 中? {is_present_set}")

# 获取集合大小 (元素数量)
set_size = len(my_set)
print(f"集合 my_set 的大小: {set_size}")

# 集合运算
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 并集 (Union): 包含两个集合中的所有元素
union_set = set_a.union(set_b) # 或者 set_a | set_b
print(f"集合 A 和 B 的并集: {union_set}")

# 交集 (Intersection): 包含两个集合中共同的元素
intersection_set = set_a.intersection(set_b) # 或者 set_a & set_b
print(f"集合 A 和 B 的交集: {intersection_set}")

# 差集 (Difference): 包含在 A 中但不在 B 中的元素
difference_set_ab = set_a.difference(set_b) # 或者 set_a - set_b
print(f"集合 A 相对于 B 的差集 (A-B): {difference_set_ab}")
difference_set_ba = set_b.difference(set_a) # 或者 set_b - set_a
print(f"集合 B 相对于 A 的差集 (B-A): {difference_set_ba}")

# 对称差集 (Symmetric Difference): 包含只在 A 或只在 B 中的元素
symmetric_difference_set = set_a.symmetric_difference(set_b) # 或者 set_a ^ set_b
print(f"集合 A 和 B 的对称差集: {symmetric_difference_set}")

# 集合是无序的，不能通过索引访问
# print(my_set[0]) # 这会引发 TypeError

# 遍历集合
print("遍历集合 my_set 中的元素:")
for item in my_set:
  print(item)

# 创建一个空集合
empty_set = set() # 注意：{} 创建的是空字典，不是空集合
print(f"这是一个空集合: {empty_set}")
