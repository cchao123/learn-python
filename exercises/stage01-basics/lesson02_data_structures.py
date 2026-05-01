# 第2课：Python 数据结构
# 对比 JavaScript：数组 → List, 对象 → Dictionary

# ==================== 1. List（类似 JavaScript 数组）====================
print("=== List（列表）===")

# 创建 List
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # 可以混合类型

print(f"水果列表: {fruits}")
print(f"数字列表: {numbers}")
print(f"混合列表: {mixed}")

# 常用操作（你试试！）
# 访问元素
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")  # 负索引，Python 特有！

# 切片（slice）- 非常强大！
print(f"前两个水果: {fruits[0:2]}")
print(f"最后两个水果: {fruits[-2:]}")

# 添加元素
fruits.append("grape")
print(f"添加葡萄后: {fruits}")

# 列表长度
print(f"列表长度: {len(fruits)}")

# ==================== 2. Tuple（不可变列表）====================
print("\n=== Tuple（元组）===")

# Tuple 创建后不能修改，类似 JavaScript 的 const 数组（更严格）
coordinates = (10, 20)
rgb = (255, 128, 0)

print(f"坐标: {coordinates}")
print(f"RGB颜色: {rgb}")

# 访问元素（和 List 一样）
print(f"X坐标: {coordinates[0]}")
print(f"Y坐标: {coordinates[1]}")

# 试试修改 Tuple（会报错！）
# coordinates[0] = 15  # 取消注释这行看看会发生什么

# ==================== 3. Set（类似 JavaScript Set）====================
print("\n=== Set（集合）===")

# Set 存储唯一值，自动去重
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_with_duplicates)

print(f"原始列表: {numbers_with_duplicates}")
print(f"去重后的Set: {unique_numbers}")

# 创建 Set
fruits_set = {"apple", "banana", "orange", "apple"}
print(f"水果Set（自动去重）: {fruits_set}")

# 添加元素
fruits_set.add("grape")
print(f"添加葡萄后: {fruits_set}")

# ==================== 4. Dictionary（类似 JavaScript 对象/Map）====================
print("\n=== Dictionary（字典）===")

# 创建 Dictionary
person = {
    "name": "cchao",
    "age": 18,
    "city": "Beijing",
    "likes_programming": True
}

print(f"个人信息: {person}")

# 访问值
print(f"名字: {person['name']}")
print(f"年龄: {person['age']}")

# 添加键值对
person["email"] = "cchao@example.com"
print(f"添加邮箱后: {person}")

# 获取所有键和值
print(f"所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")

# ==================== 5. 列表推导式（Python 特有！）====================
print("\n=== 列表推导式 ===")

# JavaScript: const squares = [1, 2, 3, 4, 5].map(x => x * x)
# Python:
squares = [x ** 2 for x in range(1, 6)]
print(f"1-5的平方: {squares}")

# 过滤偶数
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"1-10的偶数: {even_numbers}")

# ==================== 你的练习 ===================
print("\n=== 你的练习 ===")

# 练习1：创建一个存储你最喜欢编程语言的列表
favorite_languages = ['javascript', 'typescript', 'nodejs']  # 在这里添加你的列表
# 添加至少3种语言，然后打印第一个和最后一个
print(favorite_languages[0])
print(favorite_languages[-1])

# 练习2：创建一个存储你本月开销的字典
expenses = {
    "juice": 10,
    "milk": 10,
    "food": 10,
}  # 在这里添加你的字典
# 添加3项开销，比如 "food": 500, "transport": 200 等
# 然后计算总开销并打印
print(f"总消费: {sum(expenses.values())}")


# 练习3：使用列表推导式创建1-20中所有能被3整除的数
divisible_by_3 = [x for x in range(1, 21) if x % 3 == 0]  # 在这里使用列表推导式
print(f"1-20中能被3整除的数: {divisible_by_3}")


# 练习4：创建一个 Tuple 存储你的RGB颜色值
my_color = (255, 255, 255)  # 在这里创建你的颜色 Tuple
print(f"我的RGB颜色: {my_color}")
