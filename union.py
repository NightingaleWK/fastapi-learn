def process_item(item: int | str):
    if not isinstance(item, (int, str)):
        raise TypeError("item must be either int or str")
    print(item)
    print(type(item))

process_item(1)
process_item("hello")
# process_item({1: 2})  # 这行会抛出TypeError


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"发生错误：{e}")
