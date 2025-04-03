def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# 创建一个商品价格字典
prices = {
    "苹果": 5.5,
    "香蕉": 3.2,
    "橙子": 4.8
}

# 调用函数
process_items(prices)