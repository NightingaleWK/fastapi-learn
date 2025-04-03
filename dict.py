# -*- coding: utf-8 -*-

# --- 字典 (Dictionary / Dict) 示例 ---
# 字典是键值对的集合，键必须唯一且不可变（通常是字符串、数字或元组）。

# 创建一个字典
# 方法一：使用花括号 {}
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    1: "integer_key", # 键可以是数字
    (1, 2): "tuple_key" # 键可以是元组
}
print(f"初始字典: {my_dict}")

# 方法二：使用 dict() 构造函数
another_dict = dict(country="Japan", language="Python", version=3.13)
print(f"使用 dict() 创建的字典: {another_dict}")

# 访问字典中的值 (通过键)
print(f"姓名: {my_dict['name']}")
print(f"年龄: {my_dict.get('age')}") # 使用 get() 更安全，如果键不存在，返回 None (或指定默认值)
print(f"不存在的键 (使用 get): {my_dict.get('gender')}") # 输出 None
print(f"不存在的键 (使用 get 并指定默认值): {my_dict.get('gender', 'Unknown')}") # 输出 Unknown
# print(my_dict['gender']) # 直接访问不存在的键会引发 KeyError

# 添加新的键值对
my_dict["gender"] = "Female"
another_dict["framework"] = "None"
print(f"添加元素后的字典 my_dict: {my_dict}")
print(f"添加元素后的字典 another_dict: {another_dict}")

# 修改现有键的值
my_dict["age"] = 31
print(f"修改年龄后的字典 my_dict: {my_dict}")

# 删除键值对
# 方法一：使用 del 关键字
del my_dict[1] # 删除键为 1 的项
print(f"使用 del 删除键 1 后的字典: {my_dict}")

# 方法二：使用 pop() 方法 (删除并返回值)
city_value = my_dict.pop("city")
print(f"使用 pop 删除键 'city' (值为: {city_value}) 后的字典: {my_dict}")

# 方法三：使用 popitem() 方法 (删除并返回最后插入的键值对 - Python 3.7+ / 任意一项 - Python 3.6 及更早版本)
last_item = my_dict.popitem()
print(f"使用 popitem 删除最后一项 ({last_item}) 后的字典: {my_dict}")

# 获取字典的所有键
keys = another_dict.keys()
print(f"字典 another_dict 的所有键: {keys}") # 返回一个 dict_keys 对象

# 获取字典的所有值
values = another_dict.values()
print(f"字典 another_dict 的所有值: {values}") # 返回一个 dict_values 对象

# 获取字典的所有键值对 (项)
items = another_dict.items()
print(f"字典 another_dict 的所有项: {items}") # 返回一个 dict_items 对象

# 检查键是否存在
has_name = "name" in my_dict # my_dict 中 'name' 已被 popitem 删除
has_language = "language" in another_dict
print(f"'name' 是否在 my_dict 中? {has_name}")
print(f"'language' 是否在 another_dict 中? {has_language}")

# 获取字典的大小 (键值对数量)
dict_size = len(another_dict)
print(f"字典 another_dict 的大小: {dict_size}")

# 遍历字典
print("\n遍历字典 another_dict 的键:")
for key in another_dict.keys():
    print(f"键: {key}")

print("\n遍历字典 another_dict 的值:")
for value in another_dict.values():
    print(f"值: {value}")

print("\n遍历字典 another_dict 的项 (键值对):")
for key, value in another_dict.items():
    print(f"键: {key}, 值: {value}")

# 清空字典
my_dict.clear()
print(f"清空后的 my_dict: {my_dict}")

# 嵌套字典
nested_dict = {
    "person1": {"name": "Bob", "age": 25},
    "person2": {"name": "Charlie", "age": 35}
}
print(f"\n嵌套字典: {nested_dict}")
print(f"访问嵌套字典中的值: {nested_dict['person1']['name']}") # 输出 Bob

# 创建空字典
empty_dict = {}
empty_dict_alt = dict()
print(f"空字典: {empty_dict}, 类型: {type(empty_dict)}")
