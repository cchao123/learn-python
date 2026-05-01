# 第3课：Python 控制流
# 对比 JavaScript：if/else、for、while

# ==================== 1. if/else 语句 ====================
print("=== if/else 语句 ===")

# Python 用缩进和冒号，不用花括号！
age = 18

if age >= 18:
    print("你是成年人")
else:
    print("你还是未成年人")

# 多条件判断
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:  # 注意：elif 不是 else if
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"分数: {score}, 等级: {grade}")

# 逻辑运算符：and, or, not（不是 &&, ||, !）
has_ticket = True
has_id = True

if has_ticket and has_id:  # 不是 &&
    print("你可以进入电影院")
else:
    print("你不能进入电影院")

# 三元表达式（条件表达式）
age = 20
status = "成年" if age >= 18 else "未成年"  # 类似 JS 的 condition ? true : false
print(f"状态: {status}")

# ==================== 2. for 循环 ====================
print("\n=== for 循环 ===")

# 遍历列表
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"我喜欢: {fruit}")

# 遍历数字 range(start, stop, step)
# range(5) = 0, 1, 2, 3, 4（不包括5）
print("0-4的数字:")
for i in range(5):
    print(i)

# range(1, 6) = 1, 2, 3, 4, 5
print("\n1-5的数字:")
for i in range(1, 6):
    print(i)

# range(0, 10, 2) = 0, 2, 4, 6, 8（步长为2）
print("\n0-9的偶数:")
for i in range(0, 10, 2):
    print(i)

# 遍历字典
person = {"name": "cchao", "age": 18, "city": "Beijing"}

# 遍历键
print("\n遍历字典的键:")
for key in person.keys():
    print(f"键: {key}")

# 遍历值
print("\n遍历字典的值:")
for value in person.values():
    print(f"值: {value}")

# 同时遍历键和值
print("\n遍历字典的键值对:")
for key, value in person.items():
    print(f"{key}: {value}")

# enumerate 获取索引和值（类似 JS 的 forEach）
fruits = ["apple", "banana", "orange"]
print("\n带索引的遍历:")
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# ==================== 3. while 循环 ====================
print("\n=== while 循环 ===")

# 基本用法
count = 0
while count < 5:
    print(f"count: {count}")
    count += 1

print("\nwhile 循环结束")

# 无限循环（需要手动 break）
# while True:
#     print("这个会无限运行！")
#     break  # 取消注释看看

# ==================== 4. break 和 continue ====================
print("\n=== break 和 continue ===")

# break：跳出循环
print("break 示例:")
for i in range(10):
    if i == 5:
        break  # 遇到5就停止
    print(i)

# continue：跳过当前迭代
print("\ncontinue 示例:")
for i in range(5):
    if i == 2:
        continue  # 跳过2
    print(i)

# ==================== 5. for-else（Python 特有！）====================
print("\n=== for-else 语句 ===")

# else 块在循环正常结束时执行（没有被 break）
for i in range(5):
    print(i)
else:
    print("循环正常结束")

# 有 break 的情况
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("这句不会执行，因为 break 了")

# ==================== 你的练习 ===================
print("\n=== 你的练习 ===")

# 练习1：判断一个数字是正数、负数还是零
number = -5
# 在这里写你的代码
if number > 0:  # 替换这个条件
    print("正数")
elif number < 0:  # 替换这个条件
    print("负数")
else:
    print("零")


# 练习2：打印1-10之间所有的奇数
print("\n1-10的奇数:")
# 在这里用 for 循环打印
for x in range(1, 11, 2):
    print(x)

# 练习3：计算1-100的和（用 for 循环）
total = 0
# 在这里写你的循环
for x in range(1, 101):
    total += x

print(f"\n1-100的和: {total}")


# 练习4：找到列表中第一个大于5的数字并停止
numbers = [1, 3, 5, 7, 9, 2, 4, 6]
print("\n查找第一个大于5的数字:")
# 在这里用 for 循环和 break 实现
for x in numbers:
    if x > 5:
        print(x)
    break

# 练习5：猜数字游戏（简化版）
secret_number = 7
guess = 3
# 用 while 循环让用户不断猜，直到猜对（这里简化为直接判断）
# 在实际应用中可以用 input() 获取用户输入
attempts = 0
while guess != secret_number:
    guess+=1
    attempts+=1

    if guess<=secret_number:
        print('猜对了')



# 挑战题：打印九九乘法表
print("\n九九乘法表:")
# 用嵌套循环打印九九乘法表
# 提示：外层循环 1-9，内层循环 1-外层数字
for x in range(1, 10):
   for y in range(1, i + 1):
       print(f"{x} * {y}")
