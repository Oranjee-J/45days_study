# Python 基础练习题（求职面试专项）

> 🎯 本练习题共 **20 道**，覆盖 Python **基础语法、函数、类与面向对象** 三大核心模块，难度由浅入深，贴近真实面试场景。
>
> 建议独立完成后再对照答案，每题尽量手写代码。

---

## 一、基础语法篇（第 1 ~ 8 题）

### 题目 1：变量与数据类型判断

写出以下代码的输出结果，并解释原因：

```python
a = 10
b = 10.0
c = "10"

print(a == b)
print(a == c)
print(type(a), type(b), type(c))
```

---

### 题目 2：列表推导式

用 **一行代码**（列表推导式）生成一个列表，包含 1~50 中所有能被 3 整除但不能被 5 整除的数。

---

### 题目 3：字典操作

给定字典：

```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 88}
```

请完成以下操作：
1. 找出分数最高的学生姓名及分数
2. 计算所有学生的平均分（保留 2 位小数）
3. 筛选出分数 >= 90 的学生，返回新字典

---

### 题目 4：字符串处理

编写代码，将字符串 `"hello world, python is great"` 转换为 `"Hello World, Python Is Great"`（每个单词首字母大写），**不使用** `title()` 方法。

---

### 题目 5：切片与反转

给定列表 `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`，用切片操作完成：
1. 取出索引 2~7 的元素（包含两端）
2. 每隔一个取一个元素（步长为 2）
3. 反转整个列表
4. 取出最后 3 个元素

---

### 题目 6：异常处理

编写一个函数 `safe_divide(a, b)`，实现安全除法：
- 正常返回 `a / b` 的结果
- 除数为 0 时返回 `"错误：除数不能为零"`
- 参数类型错误时返回 `"错误：参数必须是数字"`

---

### 题目 7：集合运算

已知两个班级的选课名单：

```python
class_a = {"Python", "Java", "C++", "Go", "Rust"}
class_b = {"Python", "JavaScript", "Go", "TypeScript", "Rust"}
```

请用集合运算求出：
1. 两个班都选了的课程
2. 只有 A 班选了的课程
3. 两个班选课的并集
4. 只被一个班选了的课程（对称差集）

---

### 题目 8：可变与不可变对象

预测以下代码的输出结果并解释：

```python
def modify(lst, num):
    lst.append(4)
    num += 10

my_list = [1, 2, 3]
my_num = 5

modify(my_list, my_num)
print(my_list)
print(my_num)
```

---

## 二、函数篇（第 9 ~ 14 题）

### 题目 9：默认参数陷阱

以下代码有什么问题？如何修复？

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item("a"))
print(add_item("b"))
print(add_item("c"))
```

---

### 题目 10：*args 和 **kwargs

编写一个函数 `build_profile(first, last, **kwargs)`，接收名和姓，再接收任意数量的关键字参数，返回一个包含所有信息的字典。

调用示例：
```python
profile = build_profile("Albert", "Einstein", field="physics", location="Princeton")
print(profile)
# 期望输出: {'first_name': 'Albert', 'last_name': 'Einstein', 'field': 'physics', 'location': 'Princeton'}
```

---

### 题目 11：闭包

编写一个函数 `make_counter()`，每次调用返回的函数时，计数器自增 1 并返回当前计数值。

```python
counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

---

### 题目 12：装饰器

编写一个装饰器 `timer`，用于计算任意函数的执行时间（单位：秒），并打印格式如：
```
函数 xxx 执行耗时: 0.0023 秒
```

用该装饰器修饰一个对列表排序的函数并测试。

---

### 题目 13：递归函数

用递归实现一个函数 `flatten(nested_list)`，将任意嵌套的列表展平为一维列表。

```python
print(flatten([1, [2, 3], [4, [5, 6]], [[7], 8]]))
# 期望输出: [1, 2, 3, 4, 5, 6, 7, 8]
```

---

### 题目 14：高阶函数与 lambda

使用 `map()`、`filter()`、`sorted()` 和 `lambda` 完成以下任务：

给定列表：
```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 96},
]
```

1. 用 `map` 提取所有学生的姓名列表
2. 用 `filter` 筛选分数 > 80 的学生
3. 用 `sorted` 按分数从高到低排序

---

## 三、类与面向对象篇（第 15 ~ 20 题）

### 题目 15：基础类定义

定义一个 `BankAccount` 类：
- 属性：`owner`（户主）、`balance`（余额，默认 0）
- 方法：
  - `deposit(amount)`：存款，金额必须 > 0
  - `withdraw(amount)`：取款，余额不足时提示
  - `__str__`：返回格式 `"户主: xxx, 余额: xxx 元"`

---

### 题目 16：继承与方法重写

基于题目 15 的 `BankAccount`，创建子类 `SavingsAccount`（储蓄账户）：
- 新增属性：`interest_rate`（年利率，如 0.03 表示 3%）
- 新增方法：`add_interest()`，将利息加入余额
- 重写 `__str__`，额外显示年利率

---

### 题目 17：类方法与静态方法

定义一个 `Employee` 类：
- 实例属性：`name`、`salary`
- 类属性：`employee_count`（记录总员工数）、`raise_rate = 1.05`（加薪比例）
- 实例方法：`apply_raise()`，按比例加薪
- 类方法：`set_raise_rate(cls, rate)`，修改加薪比例
- 静态方法：`is_workday(day)`，判断给定日期是否为工作日（周一~周五）

---

### 题目 18：魔术方法（运算符重载）

定义一个 `Vector` 类，表示二维向量：
- 支持 `+` 运算（向量加法）
- 支持 `==` 比较
- 支持 `abs()` 求模长
- 支持 `repr()` 输出 `Vector(x, y)` 格式
- 支持 `*` 实现标量乘法（如 `v * 3`）

---

### 题目 19：属性装饰器（@property）

定义一个 `Temperature` 类：
- 内部以摄氏度存储温度
- 提供 `celsius` 属性（可读写）
- 提供 `fahrenheit` 属性（可读写，自动转换）
- 温度不能低于绝对零度（-273.15°C），设置时需校验

```python
t = Temperature(100)
print(t.celsius)       # 100
print(t.fahrenheit)    # 212.0
t.fahrenheit = 32
print(t.celsius)       # 0.0
```

---

### 题目 20：综合实战 — 简易任务管理系统

设计一个任务管理系统，包含以下类：

1. **`Task` 类**：
   - 属性：`title`、`priority`（1~5，5 最高）、`completed`（默认 False）
   - 方法：`complete()` 标记完成、`__repr__` 输出任务信息

2. **`TaskManager` 类**：
   - 管理多个 Task
   - 方法：
     - `add_task(task)`：添加任务
     - `complete_task(title)`：按标题标记任务完成
     - `get_pending()`：获取所有未完成任务（按优先级从高到低排序）
     - `get_statistics()`：返回字典 `{"total": x, "completed": y, "pending": z}`
   - 支持 `len()`：返回任务总数
   - 支持迭代（`for task in manager`）

请编写完整代码并给出使用示例。

---

## 📝 答题建议

1. **先思考再编码**：拿到题目先想清楚思路，再动手写代码
2. **注意边界情况**：如空列表、零值、类型错误等
3. **代码风格**：遵循 PEP 8 规范，变量命名清晰
4. **面试加分项**：能说出多种解法并分析优劣

祝你求职顺利！🚀
